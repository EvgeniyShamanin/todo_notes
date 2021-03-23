import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/Users.js'
import ProjectList from './components/Projects.js'
import NoteList from './components/Notes.js'
import Footer from './components/Footer.js'
import Menu from './components/Menu.js'
import Project from './components/Project.js'
import axios from 'axios'
import {BrowserRouter, Route, withRouter } from 'react-router-dom'


class App extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'notes': [],
            'project': {}
        }
    }
    usersApiRequest(){
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data.results;
                // debugger

                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
    }
    projectsApiRequest(){
        axios.get('http://127.0.0.1:8000/api/projects')
            .then(response => {
                const projects = response.data.results;
                // debugger

                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))
    }
    notesApiRequest(){
        axios.get('http://127.0.0.1:8000/api/todo')
            .then(response => {
                const notes = response.data.results;
                // debugger

                this.setState(
                    {
                        'notes': notes
                    }
                )
            }).catch(error => console.log(error))
    }
    projectApiRequest(props){
        console.log(props.match.params.uuid)
        // return <h1>Hello {props.match.params.uuid}!</h1>;
        let id = props.match.params.uuid;
        axios.get(`http://127.0.0.1:8000/api/projects/${id}`)
            .then(response => {
                const project = response.data;
                console.log(project);
                // debugger

                this.setState(
                    {
                        'project': project
                    }
                )

            }).then(() => <Project notes={this.state.project} />).catch(error => console.log(error))
    }

    componentDidMount() {
        this.usersApiRequest();
        this.projectsApiRequest();
        this.notesApiRequest();
        // this.projectApiRequest();
    }

    render() {
        return(

            <div>
                <BrowserRouter>

                        <Menu />
                        <Route exact path='/users' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todo' component={() => <NoteList notes={this.state.notes} />} />
                        <Route path="/projects/:uuid" component={this.projectApiRequest}/>
                </BrowserRouter>
                <Footer />
            </div>

        )

    }
}

export default App;
