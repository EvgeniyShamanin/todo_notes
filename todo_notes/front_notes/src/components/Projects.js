import React from 'react'
import {Link} from 'react-router-dom'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.users.map((user) => <Link to={`user/${user}`}>{user}</Link> )}
            </td>
            <td>
                {project.repository}
            </td>
            <td>
                { <Link to={`projects/${project.uuid}`}>Подробнее</Link> }
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>
                name
            </th>
            <th>
                users
            </th>
            <th>
                repository
            </th>
            <th>
                More info
            </th>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )

}


export default ProjectList
