import callAPI from "./api";

const Technicians = {
    get: data => callAPI('/api/technicians/', 'GET', data), 
    create: data => callAPI("/api/technicians/", 'POST', data),
}

export default Technicians;