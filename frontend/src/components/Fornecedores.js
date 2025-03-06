import React from 'react';
import '../App.css';


const AvaliacaoEstrelas = ({ avaliacao }) => {
    const totalEstrelas = 5;
    const estrelasCheias = Math.floor(avaliacao);
    const temMeiaEstrela = avaliacao % 1 >= 0.5;

    return (
        <div>
            {Array.from({ length: estrelasCheias }).map((_, index) => (
                <span key={index} style={{ color: 'gold', fontSize: '20px' }}>★</span>
            ))}

            {temMeiaEstrela && <span style={{ color: 'gold', fontSize: '20px' }}>⯪</span>}
            {Array.from({ length: totalEstrelas - estrelasCheias - (temMeiaEstrela ? 1 : 0) }).map((_, index) => (
                <span key={index + estrelasCheias} style={{ color: 'gray', fontSize: '20px' }}>☆</span>
            ))}
        </div>
    );
};



const Fornecedores = ({ fornecedores }) => (
    <div>
        <h2>Fornecedores Disponíveis:</h2>
        <div className="fornecedores-container">
            {fornecedores.map((fornecedor) => (
                <div className="card" key={fornecedor.id}>
                    <img
                        src={`http://localhost:5000${fornecedor.logo}`}
                        alt={`${fornecedor.nome} logo`}
                        className="logo"
                    />
                    <div>
                        <h3>{fornecedor.nome}</h3>
                        <div><strong>Estado:</strong> {fornecedor.estado}</div>
                        <div><strong>Custo por kWh:</strong> {fornecedor.custoPorKwh}</div>
                        <div><strong>Limite Mínimo de kWh:</strong> {fornecedor.limiteMinimoKwh}</div>
                        <div><strong>Número de Clientes:</strong> {fornecedor.numClientes}</div>
                        <div><strong>Avaliação Média:</strong> <AvaliacaoEstrelas avaliacao={fornecedor.avaliacaoMedia} /></div>

                    </div>
                </div>
            ))}
        </div>
    </div>
);

export default Fornecedores;