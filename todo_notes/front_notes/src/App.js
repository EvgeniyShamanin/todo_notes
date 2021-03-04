import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/Users.js'
import Footer from './components/Footer.js'
import Menu from './components/Menu.js'
import axios from 'axios'

class App extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            'users': []
        }
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))

    }

    render() {
        return(
            <div>
                <Menu />
                <UserList users={this.state.users} />
                <Footer />
            </div>
        )

    }
}

export default App;
