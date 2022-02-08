import styled from 'styled-components';
import {Link} from 'react-router-dom';

export const StyledLink = styled(Link)`
    display: flex;
    align-items: center;
    text-decoration: none;
    background-color: #55AA55;
    width: fit-content;
    padding: 5px;
    color: white;
    border-radius: 4px;
`;

export const ContainerInputFiltrar = styled.div`
    width: 100%;
    display: flex;
    border: 1px solid #DDDDDD;
    margin-bottom: 10px;

    svg {
        height: 25px;
        width: 25px;
    }
`;

export const InputFiltrar = styled.input`
    width: 100%;
    border: none;
    height: 25px;
`;

export const Formulario = styled.div`
    margin-top: 10px;
`;

export const AlunoContainer = styled.label`
    display: flex;
    justify-content: space-between;
    padding: 10px;
    border: 2px solid #e9e9f3;
    border-radius:4px;
    background-color: ${props => props.presente == 1 ? '#58c467' : props.presente == 2 ? '#d94848' : '#EEEEEE'};
    margin-bottom: 5px;
`;

export const AulaInfo = styled.div`
    background-color: #EEEEEE;
    border: 1px solid #e9e9f3;
    border-radius: 4px;
    padding: 6px;
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;

    span {
        margin-bottom: 5px;
        display: flex;
        align-items: center;
    }
`;