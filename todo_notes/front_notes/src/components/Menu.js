import React from 'react'
import '../index.css'
import {HashRouter, Link} from 'react-router-dom'



const Footer = ({}) => {
    return (
        <div className='menu'>
            <HashRouter>
                <nav>
                    <ul>
                        <li>
                            <Link to='/projects'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/users'>Users</Link>
                        </li>
                        <li>
                            <Link to='/notes'>Notes</Link>
                        </li>
                    </ul>
                </nav>
            </HashRouter>
            <p className='footer-text'>Menu</p>
        </div>
    )
}
export default Footer
