import React from 'react';

import {
    BrowserRouter as Router,
    Routes,
    Route
} from 'react-router-dom';

import PaginaInicio from './paginas';
import PaginaAulas from './paginas/aulas';
import PaginaAula from './paginas/aula';
import PaginaAlunos from './paginas/alunos';
import PaginaProfessores from './paginas/professores';



function App() {
    return (
        <>
        
        <Router>
            
            <Routes>
                <Route
                    path="/"
                    element={<PaginaInicio />}
                />

                <Route
                    path="/aulas"
                    element={<PaginaAulas />}
                />

                <Route
                    path="/aula"
                    element={<PaginaAula />}
                />

                <Route
                    path="/alunos"
                    element={<PaginaAlunos />}
                />

                <Route
                    path="/professores"
                    element={<PaginaProfessores />}
                />
            </Routes>
        </Router>
        </>
    );
}

export default App;
