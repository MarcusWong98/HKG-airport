export default async function fetch_flights(method){

    let data

    try{
        const flights_promise = await fetch('/flights', {
            method: method
        })

        const data = await flights_promise.json()
    
        console.log(data)
    }
    catch(error){
        console.error(error)
        data = null
    }


    return data



}


