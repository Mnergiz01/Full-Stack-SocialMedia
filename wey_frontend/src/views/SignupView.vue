<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">
                    Kayıt Ol
                </h1>
                <p class="mb-6 text-gray-500">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloribus, reiciendis quasi dolor eveniet
                    incidunt, hic sit beatae fuga deleniti harum enim quaerat facere voluptatibus quam dicta, libero
                    magnam neque nesciunt.
                </p>
                <p class="fone-bold">
                    Hesabınız Var Mı ? <a href="/login" class="text-blue-500 hover:text-blue-700 underline">Giriş
                        Yap</a>
                </p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" @submit.prevent="submitForm">
                    <div>
                        <label>İsim</label><br>
                        <input type="text" v-model="form.name" placeholder="Adınzı Girin"
                            class="w-full mt-2 py-4 px-6 border border-gray-300 rounded-lg">
                    </div>
                    <div>
                        <label>E-Mail</label><br>
                        <input type="email" v-model="form.email" placeholder="E-Mail Adresinizi Girin"
                            class="w-full mt-2 py-4 px-6 border border-gray-300 rounded-lg">
                    </div>
                    <div>
                        <label>Şifre</label><br>
                        <input type="password" v-model="form.password1" placeholder="Şifrenizi Girin"
                            class="w-full mt-2 py-4 px-6 border border-gray-300 rounded-lg">
                    </div>
                    <div>
                        <label>Şifre Tekrar</label><br>
                        <input type="password" v-model="form.password2" placeholder="Şifrenizi Tekrar Girin"
                            class="w-full mt-2 py-4 px-6 border border-gray-300 rounded-lg">
                    </div>
                    <template v-if="errors.length">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" :key="error">{{ error }}</p>
                        </div>
                    </template>
                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Kayıt Ol</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useToastStore } from '@/stores/toast.js'

// Form verileri
const form = ref({
    email: '',
    name: '',
    password1: '',
    password2: ''
})

// Hata mesajları
const errors = ref([])

// Toast store kullanımı
const toast = useToastStore()

// Formu gönderme işlevi
const submitForm = () => {
    errors.value = []

    // Alanları kontrol et ve hata mesajlarını oluştur
    if (form.value.email === '') {
        errors.value.push('E-Mail alanı boş olamaz')
    }
    if (form.value.name === '') {
        errors.value.push('İsim alanı boş olamaz')
    }
    if (form.value.password1 === '') {
        errors.value.push('Şifre alanı boş olamaz')
    }
    if (form.value.password2 === '') {
        errors.value.push('Şifre tekrar alanı boş olamaz')
    }
    
    // Hataları kontrol et, eğer yoksa formu gönder
    if (errors.value.length === 0) {
        axios.post('/api/signup/', form.value)
            .then(response => {
                if (response.data.message === 'success') {
                    // Form başarıyla gönderildi
                    toast.showToast(3000, 'Kayıt başarılı! Devam Etmek İçin Lütfen Giriş Yapın', ['bg-green-500', 'text-white'])
                    form.value.email = ''
                    form.value.name = ''
                    form.value.password1 = ''
                    form.value.password2 = ''
                } else {
                    // Hata durumu, backend'in başarısız yanıtı
                    toast.showToast(3000, 'Bir hata oluştu, lütfen tekrar deneyin.', ['bg-red-500', 'text-white'])
                }
            })
            .catch(error => {
                // Sunucu hatası
                console.log("Hata:", error.response.data.errors);
                console.log(error)
                toast.showToast(3000, 'Sunucu hatası, lütfen tekrar deneyin.', ['bg-red-500', 'text-white'])
            })
    } else {
        // Hata mesajlarını göster
        toast.showToast(3000, 'Lütfen tüm alanları doldurun.', ['bg-yellow-500', 'text-black'])
    }
}
</script>
