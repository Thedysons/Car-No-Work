import React from 'react'
import { Link} from "react-router-dom";
import { menuData } from '../Data/MenuData';
import logoTransBlackLong from '../img/logoTransBlackLong.png';
import {Button} from './Button';
import {FaBars} from 'react-icons/fa';
import styled from 'styled-components';
/*bunch of stuff for styling*/
const MenuBars = styled(FaBars)`
    display:none;
    @media screen and (max-width: 768px) {
        display:block;
        height: 40px;
        width: 40px;
        cursor: pointer;
        position: absolute;
        top:0;
        right:0;
        transform: translate(-50%, 25%);
    }
`
const NavMenu = styled.div`
    @media screen and (max-width: 768px) {
        display:none;
    }
`
const NavBtn = styled.div`
    @media screen and (max-width: 768px) {
        display:none;
    }
`

class NavBar extends React.Component{
    render(){
    return (
        <div className='Nav'>
            <Link to="/" className='NavMenuLinks'><img src={logoTransBlackLong} alt="logoTransBlackLong" className='logo'/></Link>
            <MenuBars>

            </MenuBars>
            <NavMenu className='NavMenu'>
                {menuData.map((item, index)=> (
                    <Link to={item.link} key={index} className='NavMenuLinks'>
                        {item.title}
                    </Link>
                ))}
            </NavMenu>
            <NavBtn className='NavBtn'>
                <Button to='/RapProfilePage' primary='true'>Push me</Button>
            </NavBtn>
        </div>
    )}
}
export default NavBar
