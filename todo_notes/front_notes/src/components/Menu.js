import React from 'react'
import '../index.css'
import {HashRouter, BrowserRouter, Link} from 'react-router-dom'



const Menu = ({}) => {
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
                    </ul>
                </nav>
            <p className='footer-text'>Menu</p>
        </div>
    )
}
export default Menu
