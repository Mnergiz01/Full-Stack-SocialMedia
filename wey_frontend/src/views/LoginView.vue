<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">
                    Giriş Yap
                </h1>
                <p class="mb-6 text-gray-500">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloribus, reiciendis quasi dolor eveniet
                    incidunt, hic sit beatae fuga deleniti harum enim quaerat facere voluptatibus quam dicta, libero
                    magnam neque nesciunt.
                </p>
                <p class="fone-bold">
                    Hesaba Sahip Değilseniz <a href="/signup" class="text-blue-500 hover:text-blue-700 underline">Kayıt
                        Ol
                    </a><span> butonuna tıklayınız</span>
                </p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" @submit.prevent="submitForm">
                    <div>
                        <label>E-Mail</label><br>
                        <input type="email" v-model="form.email" placeholder="E-Mail Adresinizi Girin"
                            class="w-full mt-2 py-4 px-6 border border-gray-300 rounded-lg">
                    </div>
                    <div>
                        <label>Şifre</label><br>
                        <input type="password" v-model="form.password" placeholder="Şifrenizi Girin"
                            class="w-full mt-2 py-4 px-6 border border-gray-300 rounded-lg">
                    </div>

                    <template v-if="errors.length">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" :key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Giriş Yap</button>
                    </div>

                </form>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref } from 'vue'
import axios from "axios";
import { useRouter } from 'vue-router'
import { useUserStore } from "@/stores/user.js"

const router = useRouter()
const form = ref({
    email: '',
    password: ''
})
const userStore = useUserStore()
const errors = ref([])

const submitForm = async () => {
    errors.value = []

    if (form.value.email === '') {
        errors.value.push('E-Mail alanı boş olamaz')
    }
    if (form.value.password === '') {
        errors.value.push('Şifre alanı boş olamaz')
    }

    if (errors.value.length === 0) {
        try {
            const response = await axios.post('/api/login/', form.value)
            userStore.setToken({
                access: response.data.access,
                refresh: response.data.refresh
            })
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access

            const meResponse = await axios.get('/api/me/')
            userStore.setUser(meResponse.data)

            router.push('/feed')
        } catch (error) {
            if (error.response && error.response.data) {
                console.log("Hata:", error.response.data)
            } else {
                console.log("Bilinmeyen hata:", error)
            }
        }
    } else {
        console.log('Alanlar boş olamaz')
    }
}
</script>
