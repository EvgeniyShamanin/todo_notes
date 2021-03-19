import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/Users.js'
import ProjectList from './components/Projects.js'
import NoteList from './components/Notes.js'
import Footer from './components/Footer.js'
import Menu from './components/Menu.js'
import axios from 'axios'
import {HashRouter, Route} from 'react-router-dom'

class App extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'notes': []
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
    componentDidMount() {
        this.usersApiRequest();
        this.projectsApiRequest();
        this.notesApiRequest();
    }

    render() {
        return(
            <div>
                <HashRouter>
                    <Menu />
                    <Route exact path='/users' component={() => <UserList users={this.state.users} />} />
                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
                    <Route exact path='/notes' component={() => <NoteList notes={this.state.notes} />} />
                </HashRouter>
                <Footer />
            </div>
        )

    }
}

export default App;
