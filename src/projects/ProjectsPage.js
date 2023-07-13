import React from 'react';
import { MOCK_PROJECTS } from './MockProjects';
import ProjectList from './ProjectList'; 
 

function ProjectsPage() {
    return (
     <>
       <h1 style={{ color:'darkblue', fontSize: '2em', marginTop: '20px', textDecoration: 'underline'}}>Airbnb Price Prediction</h1>
       <ProjectList projects={MOCK_PROJECTS} />
     </>
    );
}    

export default ProjectsPage 

