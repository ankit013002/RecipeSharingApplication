import { useState, useEffect } from "react";
import './App.css'

function App() {
    const [message, setMessage] = useState("");

    useEffect(() => {
        fetch("http://127.0.0.1:5000/")
            .then(response => response.json())
            .then(data => setMessage(data.message))
            .catch(error => console.error("Error fetching data:", error));
    }, []);

    return (
        <div>
            <h1>Recipe Sharing Application</h1>
            <p>Backend Message: {message}</p>
        </div>
    );
}

export default App;
