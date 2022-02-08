import React, {useState, useEffect} from 'react';
import axios from 'axios';

import {
    Cabecalho,
    Container,
    Lista
} from '../componentes/comuns/Componentes'

import Navbar from '../componentes/navbar/Navbar'


const baseURL = "http://localhost:5000/api";

const PaginaAlunos = () => {

    const [listaAlunos, definirListaAlunos] = useState([])

    // Seleciona os alunos
    const fetchAlunos = async () => {

        const dados = await axios.get(`${baseURL}/alunos`)
        
        const alunos = dados.data;

        definirListaAlunos(alunos);
    }

    useEffect(() => {
        fetchAlunos();
    }, [])


    
    return (
        <Container>

            <Navbar />
            
            <Cabecalho>Lista de Alunos</Cabecalho>

            <Lista>
                {listaAlunos.map((aluno, idx) => {
                    return (
                        <li key={aluno.id}>{aluno.nome} {aluno.sobrenome}</li>
                    )
                })}
            </Lista>
        </Container>
    )
};

export default PaginaAlunos;
