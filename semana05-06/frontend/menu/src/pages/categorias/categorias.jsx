import {
    Droppable,
    Draggable,
    DragDropContext
} from '@hello-pangea/dnd'
import { useEffect, useState } from 'react'
import { listarCategorias } from '../../services/categoria'

export const Categorias = () => {
    const [items, setItems] = useState([])

    useEffect(() => {
        listarCategorias().then((categorias) => {
            setItems(categorias.content)
        })
    }, [])

    const reorder = (list, start, end) => {
        const result = [...list]
        const [moved] = result.splice(start, 1)
        result.splice(end, 0, moved)
        return result
    }

    const onDragEnd = async (result) => {
        const { destination, source } = result
        if (!destination) return
        if (destination.index === source.index) return
        console.log(result)

        const categoriaId = result.draggableId
        let idVecinoProximo
        let idVecinoAnterior

        if (source.index + 1 === destination.index) {
            idVecinoAnterior = items[destination.index].id
            idVecinoProximo = items[destination.index + 1]?.id
        } else {
            if (source.index > destination.index) {
                idVecinoProximo = items[destination.index].id
                idVecinoAnterior = destination.index === 0 ? null : items[destination.index - 1].id
            } else {
                idVecinoProximo = items[destination.index + 1]?.id
                idVecinoAnterior = destination.index === 0 ? null : items[destination.index].id
            }

        }
        console.log({ categoriaId, idVecinoAnterior, idVecinoProximo })
        const data = await reordenarCategoria({ categoriaId, idVecinoAnterior, idVecinoProximo })
        console.log(data)
        setItems(prev => reorder(prev, source.index, destination.index))
    }

    return (
        <div>
            <DragDropContext onDragEnd={onDragEnd} >
                <Droppable droppableId='list' >
                    {(provided, snapshot) => (
                        <div ref={provided.innerRef} {...provided.droppableProps} style={{
                            background: snapshot.isDraggingOver ? '#f2f6ff' : '#f7f7f7',
                            padding: 12,
                            borderRadius: 10,
                            minHeight: 60,
                        }}>
                            {items.map((item, index) => (
                                <Draggable draggableId={`${item.id}`} index={index} key={item.id}>
                                    {(provided, snapshot) => (
                                        <div ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps} style={{
                                            background: '#fff',
                                            border: '1px solid #e5e5e5',
                                            color: '#000000',
                                            borderRadius: 10,
                                            padding: '12px 14px',
                                            marginBottom: 8,
                                            boxShadow: snapshot.isDragging
                                                ? '0 6px 16px rgba(0,0,0,0.12)'
                                                : '0 1px 3px rgba(0,0,0,0.06)',
                                            cursor: 'grab',
                                            ...provided.draggableProps.style,
                                        }}>
                                            {item.nombre}
                                        </div>)}
                                </Draggable>
                            ))}
                            {provided.placeholder}
                        </div>
                    )}
                </Droppable>
            </DragDropContext>
        </div>
    )
}