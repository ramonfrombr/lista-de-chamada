import React from 'react';
import {Link} from 'react-router-dom';
import styled from 'styled-components';

import {
    Cabecalho,
    Container,
    Lista
} from '../componentes/comuns/Componentes'



const PaginaInicio = () => {
  return (
    <Container>
        <Cabecalho>Painel</Cabecalho>

        <h2>Listas</h2>

        <Lista>
            <Link to="/aulas"><Icone>📖</Icone> Aulas</Link>
            <Link to="/alunos"><Icone>👨‍🎓</Icone> Alunos</Link>
            <Link to="/professores"><Icone>🧑‍🏫</Icone> Professores</Link>
        </Lista>
    </Container>

  );
};

const Icone = styled.span`
    margin-right: 10px;
`;

export default PaginaInicio;
