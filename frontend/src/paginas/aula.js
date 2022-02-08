import React, {useState, useEffect} from 'react';
import axios from 'axios';
import Moment from 'moment';
import { useLocation } from 'react-router-dom'
import {FaCalendar, FaArrowLeft, FaSearch} from 'react-icons/fa'

import {
    Cabecalho,
    Container
} from '../componentes/comuns/Componentes'

import {
    StyledLink,
    ContainerInputFiltrar,
    InputFiltrar,
    Formulario,
    AlunoContainer,
    AulaInfo,
} from '../componentes/aula/Componentes'

const baseURL = "http://localhost:5000/api";


const PaginaAula = () => {

    // Dados passados através do atributo 'state' no Link (React Router)
    const location = useLocation()
    const {
        aula_id,
        nome,
        materia,
        materia_emoji,
        lista_presenca
    } = location.state


    
    // Lista de alunos que é exibida
    const [listaAlunos, definirListaAlunos] = useState([])


    // Variável que define quais caixas estarão marcadas
    const [caixasChecadas, definirCaixasChecadas] = useState(
        new Array(lista_presenca.length).fill(false)
    );


    // Define o state da lista de alunos quando o componente for carregado
    useEffect(() => {

        // Define a lista de alunos a ser exibida como sendo a lista completa
        definirListaAlunos(lista_presenca)

        // Vetor que armazena os valores 'checked' das caixas de seleção
        let vetor = [];

        // Percorre a lista de presenca e preenche o vetor com TRUE ou FALSE
        lista_presenca.map(presenca => {

            vetor.push(presenca.presente != 1 ? false : true);
        })

        definirCaixasChecadas(vetor);
    }, [])
 


    const handleFiltrarLista = (evento) => {

        // Cria um RegEx com o valor digitado
        const regex = new RegExp(evento.target.value.toLowerCase());
        
        // Cria uma lista com os alunos que atendem ao regex
        const lista_filtrada = lista_presenca.filter(
            presenca => [presenca.aluno.nome, presenca.aluno.sobrenome].join(' ').toLowerCase().match(regex)) 


        // Define a lista a ser exibida
        definirListaAlunos(lista_filtrada);

        // Vetor que armazena os valores 'checked' das caixas de seleção
        let vetor = [];

        // Percorre a lista de presenca e preenche o vetor com TRUE ou FALSE
        lista_filtrada.map(presenca => {

            vetor.push(presenca.presente != 1 ? false : true);
        })

        definirCaixasChecadas(vetor);
    }


    const handleAlteracaoPresenca = async posicao => {
        
        // posição é o índice do aluno no vetor


        const caixasAtualizadas = caixasChecadas.map((item, index) =>
          index === posicao ? !item : item
        );

        // Altera o valor da caixa
        definirCaixasChecadas(caixasAtualizadas);


        // Seleciona o índice do aluno que foi clicado na lista completa
        let indice = lista_presenca.findIndex(elemento => elemento.aluno_id == listaAlunos[posicao].aluno_id)

        // Atualiza o valor presente na lista de alunos completa
        lista_presenca[indice].presente = caixasAtualizadas[posicao] == true ? 1 : 2;

        // Prepara o objeto a ser enviado
        const dados_enviados = {
            "nome_usuario": listaAlunos[posicao].aluno.nome_usuario,
            "presente": caixasAtualizadas[posicao] == true ? 1 : 2
        }

        // Envia a alteração da presença
        await axios.put(
            `${baseURL}/aulas/${aula_id}/presenca`,
            dados_enviados
        )
    };




    return (
        <Container>

            <StyledLink
                to='/aulas'
            >
                <FaArrowLeft />
            </StyledLink>

            <Cabecalho>{nome}</Cabecalho>

            <AulaInfo>
                <span>Matéria: {materia_emoji} {materia}</span>
            </AulaInfo>

            <h3>Lista de Presença</h3>

            <ContainerInputFiltrar>
                <InputFiltrar
                    onChange={handleFiltrarLista}
                />
                
                <FaSearch />
            </ContainerInputFiltrar>

            <Formulario
            >
                {listaAlunos.map((presenca, index) => {
                    return (
                        <AlunoContainer
                            key={presenca.aluno.id}
                            htmlFor={presenca.aluno.nome_usuario}
                            presente={presenca.presente}
                        >

                            <span>{presenca.aluno.nome} {presenca.aluno.sobrenome}</span>
                          
                            <input
                                type="checkbox"
                                onChange={() => handleAlteracaoPresenca(index)}
                                checked={caixasChecadas[index]}
                                name={presenca.aluno.nome_usuario}
                                id={presenca.aluno.nome_usuario}
                                
                            />
                            
                        </AlunoContainer>
                    )
                })}
            </Formulario>
        </Container>
    );
};

export default PaginaAula;
