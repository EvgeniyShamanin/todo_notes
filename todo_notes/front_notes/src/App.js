import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/Users.js'
import ProjectList from './components/Projects.js'
import NoteList from './components/Notes.js'
import Footer from './components/Footer.js'
import Menu from './components/Menu.js'
import Project from './components/Project.js'
import LoginForm from './components/Auth.js'
import axios from 'axios'
import {BrowserRouter, Route, withRouter } from 'react-router-dom'
import Cookies from 'universal-cookie';


class App extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'notes': [],
            'project': {},
            'auth': {username: '', is_login: false}
        }
    }

    set_token(token, username) {
        const cookies = new Cookies()
        cookies.set('token', token);
        cookies.set('username', username);
    }

    logout() {
        this.set_token('', '')
        this.setState({'auth': {username: '', is_login: false}})
        this.setState({'users': []})
        this.setState({'projects': []})
        this.setState({'notes': []})
        this.load_data()
    }

    get_token_from_storage() {
        const cookies = new Cookies();
        const username = cookies.get('username');
        if ((username != "") & (username != null)) {
            this.setState({'auth': {username: username, is_login: true}}, () => this.load_data())
        }
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'], username);
                this.setState({'auth': {username: username, is_login: true}})
                this.load_data()
            }).catch(error => alert('Неверный логин или пароль'))
    }

    load_data() {
        let headers = {
            'Content-Type': 'application/json'
        };
        if (this.state.auth.is_login){
            const cookies = new Cookies();
            const token = cookies.get('token');
            headers['Authorization'] = 'Token ' + token
        }
        axios.get('http://127.0.0.1:8000/api/users', {headers})
            .then(response => {
                const users = response.data.results;
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/projects', {headers})
            .then(response => {
                const projects = response.data.results;
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/todo', {headers})
            .then(response => {
                const notes = response.data.results;
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

        this.get_token_from_storage()

    }

    render() {
        return(

            <div>
                <BrowserRouter>

                        <Menu state={this.state} logout={() => this.logout()}/>
                        <Route exact path='/users' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todo' component={() => <NoteList notes={this.state.notes} />} />
                        <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                        <Route path="/projects/:uuid" component={this.projectApiRequest}/>
                </BrowserRouter>
                <Footer />
            </div>

        )

    }
}

export default App;
