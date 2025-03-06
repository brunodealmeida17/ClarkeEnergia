// src/App.js
import React, { useState, useEffect } from 'react';
import { useQuery } from '@apollo/client';
import FormularioConsumo from './components/FormularioConsumo';
import Fornecedores from './components/Fornecedores';
import './App.css';
import { GET_FORNECEDORES } from './graphql/queries';

const App = () => {
  const [consumo, setConsumo] = useState(null);
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    document.body.className = darkMode ? 'dark' : 'light';
  }, [darkMode]);

  const { data, loading, error } = useQuery(GET_FORNECEDORES, {
    variables: { consumo },
    skip: consumo === null,
  });

  const handleConsumoSubmit = (valorConsumo) => {
    setConsumo(parseInt(valorConsumo));
  };

  return (
    <div>
      <button
        className="toggle-button"
        onClick={() => setDarkMode(!darkMode)}
      >
        {darkMode ? 'Modo Claro' : 'Modo Escuro'}
      </button>

      <h1>Informe seu consumo de energia e encontre os melhores fornecedores!</h1>
      <FormularioConsumo onSubmit={handleConsumoSubmit} />
      {loading && <p>Carregando...</p>}
      {error && <p>Erro: Estamos enfrentando um problema no servidor. Já estamos cientes e trabalhando para resolvê-lo.</p>}
      {data && <Fornecedores fornecedores={data.fornecedores} />}
    </div>
  );
};

export default App;
