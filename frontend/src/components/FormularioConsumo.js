import React, { useState } from 'react';
import '../App.css';

const FormularioConsumo = ({ onSubmit }) => {
    const [consumo, setConsumo] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(consumo);
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Consumo mensal de energia (kWh):
                <input
                    type="number"
                    value={consumo}
                    onChange={(e) => setConsumo(e.target.value)}
                    min="1"
                    required
                />
            </label>
            <button type="submit" className="button">Enviar</button>
        </form>
    );
};

export default FormularioConsumo;