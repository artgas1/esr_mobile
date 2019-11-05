import callAPI from "./api";

const Clinics = {
    get: data => callAPI('/api/clinics/', 'GET', data), 
    create: data => callAPI("/api/clinics/", 'POST', data),
}

export default Clinics;