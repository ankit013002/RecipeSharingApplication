import { useState, useEffect } from "react";
import './App.css'

function App() {
    const [message, setMessage] = useState("");

    const handleClick = async () => {
        const data = {
            title: "Latest",
            description: "This is a test doc",
            created_at: new Date().toISOString(),
        };
        console.log(data);
        try {
            const response = await fetch("http://127.0.0.1:5000/add-document",{
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();
            console.log("Got Result")
            console.log(result.Success)
            if (result.Success) {
                console.log("True");
                setMessage(`Document added! ID: ${result.doc_id}`);
            } else {
                console.log("False");
                setMessage(`Error: ${result.error}`);
            }
        }
        catch (error) {
            setMessage("Request failed: " + error.message);
        }

    }

    useEffect(() => {
        // Polling mechanism to fetch data every 2 seconds
        const interval = setInterval(() => {
            fetch("http://127.0.0.1:5000/get-document")
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    setMessage(`born: ${data.data}`)
                })
                .catch(error => console.error("Error fetching data:", error));
        }, 2000);  // Polls the backend every 2 seconds

        return () => clearInterval(interval); // Cleanup interval on component unmount
    }, []);

    return (
        <div>
            <h1>Recipe Sharing Application</h1>
            <button onClick={() => handleClick()}>Click Me</button>
            <p>Backend Message: {message}</p>
        </div>
    );
}

export default App;
