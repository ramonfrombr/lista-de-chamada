import React, {useState, useEffect} from 'react';
import axios from 'axios';
import {Link} from 'react-router-dom';
import Moment from 'moment';

import {
    FaCalendar,
    FaUsers
} from 'react-icons/fa';

import {
    Cabecalho,
    Container,
    Lista
} from '../componentes/comuns/Componentes'

import {
    AulaNome,
    AulaRodape,
    AulaRodapeInfo
} from '../componentes/aulas/Componentes'

import Navbar from '../componentes/navbar/Navbar'

const baseURL = "http://localhost:5000/api";



const PaginaAulas = () => {

    Moment.locale('pt');

    const [listaAulas, definirListaAulas] = useState([])

    // Seleciona as aulas
    const fetchAulas = async () => {
        
        const dados = await axios.get(`${baseURL}/aulas`)

        const aulas = dados.data;

        definirListaAulas(aulas);
    }


    useEffect(() => {
        fetchAulas();
    }, [])
    
    return (
        

        <Container>

            <Navbar />

            <Cabecalho>Lista de Aulas</Cabecalho>
            
            <Lista>
                {listaAulas.map((aula, idx) => {
                    return (
                        <Link
                            key={aula.id}
                            to={"/aula"}
                            state={{
                                    aula_id: aula.id,
                                    nome: aula.nome,
                                    materia: aula.materia.nome,
                                    materia_emoji: aula.materia.emoji,
                                    lista_presenca: aula.lista_presenca,
                                }}
                        >
                            <AulaNome>{aula.nome}</AulaNome>

                            <AulaRodape>
                                <AulaRodapeInfo>
                                    <FaUsers />&nbsp;{aula.alunos.length} alunos
                                </AulaRodapeInfo>

                            </AulaRodape>
                        </Link>
                    )
                })}
            </Lista>
        </Container>
    )
};

export default PaginaAulas;
