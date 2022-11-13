<script>
import axios from "axios";

export default axios.create({
  baseURL: import.meta.env.VITE_API_ENDPOINT,
  //   baseURL: "http://127.0.0.1:5000",
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    // 'Access-Control-Allow-Credentials':true
    // "User-Email": sessionStorage.getItem('logInResponse') ? JSON.parse(sessionStorage.getItem('logInResponse')).username : null
  },
});
</script>
