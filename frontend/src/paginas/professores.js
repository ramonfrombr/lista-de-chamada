import React, {useState, useEffect} from 'react';
import axios from 'axios';


import {
    Cabecalho,
    Container,
    Lista
} from '../componentes/comuns/Componentes'

import Navbar from '../componentes/navbar/Navbar'



const baseURL = "http://localhost:5000/api";


const PaginaProfessores = () => {

    const [listaProfessores, definirListaProfessores] = useState([])
       
    // Seleciona os alunos
    const fetchProfessores = async () => {

        const dados = await axios.get(`${baseURL}/professores`)
        
        const professores = dados.data;

        definirListaProfessores(professores);
    }

    useEffect(() => {
        fetchProfessores();
    }, [])



    return (
        <Container>
            <Navbar />

            <Cabecalho>Lista de Professores</Cabecalho>

            <Lista>
                {listaProfessores.map((professor, idx) => {
                    return (
                        <li key={professor.id}>{professor.nome} {professor.sobrenome}</li>
                    )
                })}
            </Lista>
        </Container>
    )
};

export default PaginaProfessores;
