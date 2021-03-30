import React from 'react'


const NoteItem = ({note}) => {
    // debugger
    return (
        <tr>
            <td>
                {note.text}
            </td>
            <td>
                {
                    note.project.name

                }
            </td>
            <td>
                {note.created}
            </td>
            <td>
                {note.updated}
            </td>
            <td>
                {note.user}
            </td>
            <td>
                {note.status}
            </td>
        </tr>
    )
}

const NoteList = ({notes}) => {
//    debugger
    return (
        <table>
            <th>
                text
            </th>
            <th>
                project
            </th>
            <th>
                created
            </th>
            <th>
                updated
            </th>
            <th>
                user
            </th>
            <th>
                status
            </th>
            {notes.map((note) => <NoteItem note={note} />)}
        </table>
    )

}


export default NoteList
