import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000"
});

export default API;

// ADD THIS
export const downloadCSV = () => {
  window.open("http://127.0.0.1:5000/download", "_blank");
};