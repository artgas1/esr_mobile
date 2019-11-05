import callAPI from "./api";

const Doctors = {
    get: data => callAPI('/api/doctors/', 'GET', data), 
    create: data => callAPI("/api/doctors/", 'POST', data),
}

export default Doctors;