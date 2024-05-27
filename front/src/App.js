import React, { useEffect, useState } from 'react';
import { Client } from './client';
import './App.css';


function Song(props){

  console.log(props);
  const position = props.position;
  const playSong=()=>{
    let client = new Client("http://localhost:8000");
    client.playSong(position, (data)=>{
        console.log("playing");
    });
  };

  return <tr><td>{props.title}</td>
           <td><i className="bi bi-play-fill" onClick={playSong}></i></td>
           <td><i className="bi bi-trash"></i></td>
         </tr>
 }

function App() {


  const [songs, setSongs] = useState([]);


  useEffect(() => {

    fetch("http://localhost:8000/api/songs")
      .then(response => { return response.json() })
      .catch(error => console.log(error))
      .then(response => {
        console.log(response);
        setSongs(response);
      })
  }, []);

  const addFile = () => {
    let fileValue = document.getElementById("fileselect").value;
    console.log(fileValue);
  }
  const selectFile = () => {
    const fileSelector = document.getElementById("fileselect");
    fileSelector.click();
    fileSelector.onchange = addFile;
  };


  const stopPlay = ()=>{
    let client = new Client("http://localhost:8000");
    client.stop(()=>{
      console.log("Stopping");
    });
  }
  const nextSong = ()=>{
    let client = new Client("http://localhost:8000");
    client.next(()=>console.log("next"));
  }

  const prevSong=() =>{
    let client = new Client("http://localhost:8000");
    client.prev(()=> console.log("prev"))
  }
  return (
    <div className="container">
      <div>
        <input type="file" id="fileselect" />
        <button className='btn btn-primary' onClick={selectFile}>Añadir...</button>
        <br />
        <div className='buttons-controllers'>
          <button className="btn btn-success" onClick={prevSong}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-rewind" viewBox="0 0 16 16">
              <path d="M9.196 8 15 4.633v6.734zm-.792-.696a.802.802 0 0 0 0 1.392l6.363 3.692c.52.302 1.233-.043 1.233-.696V4.308c0-.653-.713-.998-1.233-.696z" />
              <path d="M1.196 8 7 4.633v6.734zm-.792-.696a.802.802 0 0 0 0 1.392l6.363 3.692c.52.302 1.233-.043 1.233-.696V4.308c0-.653-.713-.998-1.233-.696z" />
            </svg>
          </button>
          <button className='btn btn-danger' onClick={stopPlay}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-stop-fill" viewBox="0 0 16 16" >
              <path d="M5 3.5h6A1.5 1.5 0 0 1 12.5 5v6a1.5 1.5 0 0 1-1.5 1.5H5A1.5 1.5 0 0 1 3.5 11V5A1.5 1.5 0 0 1 5 3.5" />
            </svg>
          </button>
          <button className='btn btn-success' onClick={nextSong}>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-fast-forward-fill" viewBox="0 0 16 16" >
              <path d="M7.596 7.304a.802.802 0 0 1 0 1.392l-6.363 3.692C.713 12.69 0 12.345 0 11.692V4.308c0-.653.713-.998 1.233-.696z" />
              <path d="M15.596 7.304a.802.802 0 0 1 0 1.392l-6.363 3.692C8.713 12.69 8 12.345 8 11.692V4.308c0-.653.713-.998 1.233-.696z" />
            </svg>
          </button>
        </div>
      </div>
      <table>
        <thead>
          <tr><td>Song</td>
            <td></td>
            <td></td></tr>
        </thead>
        <tbody>
          {songs.map((row) => <Song title={row.title} position={row.position} />)}
        </tbody>
      </table>
    </div>
  );
};




export default App;
