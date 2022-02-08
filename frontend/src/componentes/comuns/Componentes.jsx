import styled from 'styled-components';


export const Cabecalho = styled.h1`
    text-align: center;
`;

export const Container = styled.div`
    padding: 10px;

    @media (min-width: 768px) {
        width: 70%;
        margin: 0 auto;
    }
`;

export const Lista = styled.div`
    display: flex;
    flex-direction: column;

    > a, > div, > li {
        list-style: none;
        border: 2px solid #e9e9f3;
        border-radius:4px;
        padding: 10px;
        margin-bottom: 5px;
        text-decoration: none;
        color: black;
        background-color: #F1F1F1;
    }

  
`