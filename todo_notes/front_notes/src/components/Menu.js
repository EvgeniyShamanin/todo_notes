import React from 'react'
import '../index.css'
import {HashRouter, BrowserRouter, Link} from 'react-router-dom'



const Menu = ({state, logout}) => {
    return (
        <div className='menu'>
                <nav>
                    <ul>
                        <li>
                            <Link to='/projects'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/users'>Users</Link>
                        </li>
                        <li>
                            <Link to='/todo'>Notes</Link>
                        </li>
                        <li>
                            {state.auth.is_login ? <button onClick={()=>logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                        </li>
                    </ul>
                </nav>
            <p className='footer-text'>Menu</p>
        </div>
    )
}
export default Menu
