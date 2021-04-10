import React from 'react'
import {
    useParams
} from "react-router-dom";

const ProjectItem = ({getProject, item}) => {
    // debugger
    let { uuid } = useParams();
    // debugger
    getProject(uuid)
    // debugger
    return (
        <div>{item.name}</div>
    )
};

export default ProjectItem
