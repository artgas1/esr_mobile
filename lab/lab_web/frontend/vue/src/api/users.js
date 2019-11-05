import callAPI from './api'
const Users = {
  get: id => callAPI(`/api/users/${id}/`, 'get'),
  getCurrent: () => callAPI(`/api/users/current/`, 'get'),
  updateCurrent: data => callAPI("/api/users/current/", "put", data),
  deleteCurrent: data => callAPI("/api/users/current/", "delete", data),
}
export default Users
