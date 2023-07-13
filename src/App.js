import React, { useState } from "react";
import Papa from "papaparse";

/*import React from 'react';
import ProjectsPage from './projects/ProjectsPage';
//import './App.css';

function App() {
    return (
    <div className="container">
      <ProjectsPage />
    </div>
    );
}

export default App; */  


function App() {
  const [file, setFile] = useState();
  const [array, setArray] = useState([]);
  const [predictions, setPredictions] = useState([]);

  const fileReader = new FileReader();

  const handleOnChange = (e) => {
    setFile(e.target.files[0]);
     Papa.parse(e.target.files[0], {
     header: true,
     skipEmptyLines: true,
     complete: function (results) {
       console.log(results.data)
     },
   });    
  };
        


  const csvFileToArray = (string) => {
    Papa.parse(string, {
      header: true,
      skipEmptyLines: true,
      complete: function (results) {
        //console.log('Parsing Results:', results);
        if (Array.isArray(results.data)) {
          const parsedArray = results.data.map((row) => {
            const obj = {};
            for (let key in row) {
              obj[key.trim()] = row[key].trim();
            }
            return obj;
          });
          setArray(parsedArray);
        } else {
          console.error('Error parsing CSV data.');
        }
      },  
    });
  };
  
  
  const handleOnSubmit = (e) => {
    e.preventDefault();

    if (file) {
      fileReader.onload = function (event) {
        const text = event.target.result;
        csvFileToArray(text);
      };

      fileReader.readAsText(file); 
    }
  };


  const handlePredict = async (event) => {
    console.log('array',array) 
    event.preventDefault()
    try { 
      const response = await fetch('/multi_airpredict', {                                                                                             
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(array),
      });

      if (!response.ok) {
        throw new Error('Prediction failed');
      }


      const data = await response.json();
      console.log(data);
      if (Array.isArray(data)) { // Check if data is an array
        setPredictions(data); // Set predictions directly from the response
      } else {
        console.error("Invalid predictions data format");
      }  
      //setPredictions(data.predictions);
    } catch (error) {
      console.log(error);
    } 
  };

  const headerKeys = Object.keys(Object.assign({}, ...array));

  return (
    <div style={{ textAlign: 'center' }}>    
      <h1 style={{ color:'darkblue', fontSize: '2em', marginTop: '5px', textDecoration: 'underline'}}>Airbnb Price Prediction</h1>
      <form>
        <input
          type="file"
          id="csvFileInput"
          accept=".csv"
          onChange={handleOnChange}
        />
        <button onClick={handleOnSubmit}>IMPORT CSV</button>
        <button onClick={handlePredict}>PREDICT</button>
      </form>

      <br />
        
      <table>
        <thead>
          <tr key="header">
            {headerKeys.map((key) => (
              <th key={key}>{key}</th>
            ))}
          </tr>
        </thead>

       <tbody>
          {array.map((item, index) => (
            <tr key={index}>
              {Object.values(item).map((val, index) => (
                <td key={index}>{val}</td>
              ))}
            </tr>  
          ))}
        </tbody> 
      </table>

                
      <div>
        <h2 style={{ textAlign: 'left',color:'blue', fontSize: '1.5em', marginTop: '3px', textDecoration: 'underline'}}>Predictions</h2>
         <ul style={{ textAlign: 'left'}}>
          {predictions.map((prediction, index) => (
            <li key={index}>{prediction}</li>
          ))}
         </ul>
      </div>
    </div>
  );
}

export default App; 






