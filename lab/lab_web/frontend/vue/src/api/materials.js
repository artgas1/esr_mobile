import callAPI from "./api";

const Materials = {
    get: data => callAPI('/api/materials/', 'GET', data),
    create: data => callAPI("/api/materials/", 'POST', data),
    UsedOnOperation: {
        create: data => callAPI('/api/materials_used_on_operation/', 'POST', data),
    }
}

export default Materials;