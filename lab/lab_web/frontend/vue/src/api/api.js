import axios from 'axios';

const API_HOST = "127.0.0.1:8000";
const HTTPS = false;
function callAPI(path, method, data, config){
  data = data || {};
  config = config || {};
  const protocol = HTTPS ? "https" : "http";
  let headers = {};
  if(localStorage.token){
    headers["Authorization"] = `Token ${localStorage.token}`;
  }
  return axios(Object.assign({
    method: method,
    url: `${protocol}://${API_HOST}${path}`,
    data: data,
    headers: headers,
  }, config));
}
export default callAPI;
