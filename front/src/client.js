
export class Client{

    constructor(url){
        this.url=url;
    }

    getSongList(callback){
        fetch(this.url+"/api/songs",
            {
                method:"GET"
            }
        ).then(response => response.json())
        .catch(error => console.log(error))
        .then(response => callback(response))
    }

    addSong(file, callback){
        const data = {
            song: file
        }
        fetch(this.url+'/api/songs',{
            method: "POST",
            body: JSON.stringify(data)
        })
        .then(response=> response.json())
        .then(response => callback(response))
        .catch(error=> console.log(error))
    }

    playSong(index, callback){
        fetch(this.url+'/api/play/'+index)
        .then(response=> response.json())
        .then(response => callback(response))
        .catch(error=> console.log(error))
    }

    stop(callback){
        fetch(this.url+'/api/stop/')
        .then(response=> response.json())
        .then(response => callback(response))
        .catch(error=> console.log(error))
    }

    next(callback){
        fetch(this.url+'/api/next')
        .then(response=> response.json())
        .then(response => callback(response))
        .catch(error=> console.log(error))
    }

    prev(callback){
        fetch(this.url+'/api/prev')
        .then(response=> response.json())
        .then(response => callback(response))
        .catch(error=> console.log(error))
    }
}