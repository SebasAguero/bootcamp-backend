from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Album, Archivo, Recuerdo
from .serializers import AlbumSerializer, RecuerdoSerializer, RutaFirmadaSerializer, ArchivoSerializer
from boto3 import session
from os import environ

class GestionAlbum(ListCreateAPIView):
    # Asi indicamos que solo vamos a listar los albumnes cuyo finalizado sea True
    queryset = Album.objects.filter(finalizado=True).all()
    serializer_class = AlbumSerializer


@api_view(http_method_names=['PUT'])
def alternarAlbumEstado(request: Request, id):
    # En base al id que tengamos por la url `/alternar-estado-albumn/123abc`
    # modificar el valor de finalizado y si es verdadero ponerlos a falso y viceversa
    albumEncontrado = Album.objects.filter(id=id).first()
    if not albumEncontrado:
        return Response(data={
            'message':'Album no encontrado'
        },status=status.HTTP_400_BAD_REQUEST)
    
    # Por ser un boolean podemos alternar el valor del finalizado con la palabra `not`
    albumEncontrado.finalizado = not albumEncontrado.finalizado

    albumEncontrado.save()
    result = AlbumSerializer(instance=albumEncontrado)

    return Response(data={
        'message':'Estado modificado exitosamente',
        'content':result.data
    })


class GestionRecuerdo(APIView):
    def post(self, request):
        serializer = RecuerdoSerializer(data=request.data)
        if serializer.is_valid():
            # al momento de hacer la serializacion y pasarle una FK el serializador obtiene la informacion y la busca en la bd, es decir, el albumId ya es una instancia del modelo Album
            albumId = serializer.validated_data.get('albumId')

            if albumId.finalizado:
                return Response(data={
                    'message':'El album ya esta finalizado y no se puede continuar'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Podemos usar el serializador para guardar la informacion en la bd
            serializer.save()

            return Response(data={
                'message':'Recuerdo creado exitosamente',
                'content': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response(data={
                'message':'Error al crear el recuerdo',
                'content':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def crearRutaFirmadaArchivo(request: Request):
    serializer = RutaFirmadaSerializer(data=request.data)

    if serializer.is_valid():
        s3 = session.Session(
            aws_access_key_id=environ.get('S3_ACCESS_KEY'),
            aws_secret_access_key=environ.get('S3_SECRET_KEY'),
            region_name=environ.get('S3_REGION')
        ).client('s3')
        
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/generate_presigned_url.html
        url = s3.generate_presigned_url(
            ClientMethod='put_object', 
            Params={
                "Bucket": environ.get('S3_BUCKET'),
                "Key":serializer.validated_data.get('key'),
                "ContentType":serializer.validated_data.get('contentType')
            },
            ExpiresIn=600)
        
        return Response({
            'content': url
            })
    
    else:
        return Response({
            'message':'Error al generar la url firmada',
            'content': serializer.errors
        })
    


class GestionArchivos(APIView):
    def post(self, request:Request):
        serializer = ArchivoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data={
                'message':'Archivo creado exitosamente',
                'content':serializer.data
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message':'Error al crear el archivo',
                'content': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request:Request):
        archivos = Archivo.objects.all()
        s3 = session.Session(
            aws_access_key_id=environ.get('S3_ACCESS_KEY'),
            aws_secret_access_key=environ.get('S3_SECRET_KEY'),
            region_name=environ.get('S3_REGION')
        ).client('s3')

        resultado = []

        for archivo in archivos:
            url = s3.generate_presigned_url(
                ClientMethod='get_object', 
                Params={
                "Bucket": environ.get('S3_BUCKET'),
                "Key": f"{archivo.path if archivo.path is not None else '' }{archivo.key}.{archivo.extension}"
                }, 
                ExpiresIn= 3600 # Segundos expresados en numeros
            )
            resultado.append({
                'archivo': archivo.key,
                'url': url
            })

        return Response(data=resultado)


class GestionArchivo(APIView):
    def get(self,request:Request, id):
        
        archivoEncontrado = Archivo.objects.filter(id=id).first()
        if not archivoEncontrado:
            return Response(data={
                'message':'Archivo no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        s3 = session.Session(
            aws_access_key_id=environ.get('S3_ACCESS_KEY'),
            aws_secret_access_key=environ.get('S3_SECRET_KEY'),
            region_name=environ.get('S3_REGION')
        ).client('s3')

        url = s3.generate_presigned_url(
                ClientMethod='get_object', 
                Params={
                "Bucket": environ.get('S3_BUCKET'),
                "Key": f"{archivoEncontrado.path if archivoEncontrado.path is not None else '' }{archivoEncontrado.key}.{archivoEncontrado.extension}"
                }, 
                ExpiresIn= 3600
        )

        return Response(data={
            "url": url,
            "key": archivoEncontrado.key
        })

    def delete(self,request,id):
        archivoEncontrado = Archivo.objects.filter(id=id).first()
        if not archivoEncontrado:
            return Response(data={
                'message':'Archivo no encontrado'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        archivoEncontrado.delete()

        s3 = session.Session(
            aws_access_key_id=environ.get('S3_ACCESS_KEY'),
            aws_secret_access_key=environ.get('S3_SECRET_KEY'),
            region_name=environ.get('S3_REGION')
        ).client('s3')

        s3.delete_object(
            Bucket=environ.get('S3_BUCKET'),
            Key=f"{archivoEncontrado.path if archivoEncontrado.path is not None else '' }{archivoEncontrado.key}.{archivoEncontrado.extension}"
        )

        return Response(data={
            'message':'Archivo eliminado exitosamente'
        })