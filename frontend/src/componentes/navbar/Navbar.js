import React from 'react';
import styled from 'styled-components';
import {Link} from 'react-router-dom';

import {FaArrowLeft} from 'react-icons/fa'

const Navbar = () => {
    return (
        <StyledLink to='/'>
            <FaArrowLeft />
        </StyledLink>
    );
};


const StyledLink = styled(Link)`
    display: flex;
    align-items: center;
    text-decoration: none;
    background-color: #55AA55;
    width: fit-content;
    padding: 5px;
    color: white;
    border-radius: 4px;
`;



export default Navbar;
