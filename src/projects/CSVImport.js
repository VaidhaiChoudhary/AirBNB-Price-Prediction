import React from 'react';

function CSVImport() {
    return (
      <div>
        <h1>CSV Import</h1>
        <form>
          <input type={"file"} accept={".csv"} />
          <button>IMPORT CSV</button>
        </form>
      </div>
    );
  }
  
  export default CSVImport;



