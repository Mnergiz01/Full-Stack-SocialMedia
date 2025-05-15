// stores/user.js
import { defineStore } from "pinia";
import axios from "axios";

export const useUserStore = defineStore('user',{
  id: "user",

  state: () => ({
    isAuthenticated: false,
    id: null,
    name: null,
    email: null,
    access: null,
    refresh: null,
  }),

  actions: {
    initStore() {
      console.log("initStore",localStorage.getItem("user.access"))
      if (localStorage.getItem("user.access")) {
        this.access = localStorage.getItem("user.access");
        this.refresh = localStorage.getItem("user.refresh");
        this.id = localStorage.getItem("user.id");
        this.name = localStorage.getItem("user.name");
        this.email = localStorage.getItem("user.email");
        this.isAuthenticated = true;
        this.refreshToken();
      }
    },
    setUser(data) {
      this.id = data.id;
      this.name = data.name;
      this.email = data.email;
    
      localStorage.setItem("user.id", data.id);
      localStorage.setItem("user.name", data.name);
      localStorage.setItem("user.email", data.email);
    
      console.log('initialized user - id:', this.id)
      console.log('initialized user - name:', this.name)
      console.log('initialized user - email:', this.email)
    },

    setToken(data) {
      console.log('setToken' , data)
      this.access = data.access;
      this.refresh = data.refresh;
      this.isAuthenticated = true;

      localStorage.setItem("user.access", data.access);
      localStorage.setItem("user.refresh", data.refresh);
      
      console.log(localStorage.getItem('user.access'))
    },

    removeToken() {
      this.access = null;
      this.refresh = null;
      this.isAuthenticated =false;
      this.id = null;
      this.name = null;
      this.email = null;

      localStorage.removeItem("user.access");
      localStorage.removeItem("user.refresh");
      localStorage.removeItem("user.id");
      localStorage.removeItem("user.name");
      localStorage.removeItem("user.email");
    },

    refreshToken() {
      axios
        .post("/api/refresh/", {
          refresh: this.refresh,
        })
        .then((response) => {
          this.access = response.data.access;
          localStorage.setItem("user.access", response.data.access);
          axios.defaults.headers.common["Authorization"] =
            "Bearer " + response.data.access;
        })
        .catch((error) => {
          console.log("refresh token error : ", error);
          this.removeToken();
        });
    },
    logout() {
      this.removeToken()
    },
  },
});
