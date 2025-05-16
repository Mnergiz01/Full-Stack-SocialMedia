<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg text-center">
                <img src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=300&h=300&q=80"
                    class="mb-6 rounded-full" alt="User Avatar">
                <p><strong>{{ user.name }}</strong></p>
                <div class="mt-6 flex space-x-8 justify-around">
                    <router-link :to="{ name: 'friends', params: { id: user.id } }"
                        class="text-xs text-gray-500">
                        {{ friends.length }} Arkadaş
                    </router-link>
                    <p class="text-xs text-gray-500">120 Post</p>
                </div>
            </div>
        </div>
        <div class="main-center col-span-2 space-y-4">
            <div class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4" v-if="requests.length">
                <div class="p-4 bg-white border border-gray-200 text-center rounded-lg" v-for="reqUser in requests"
                    :key="reqUser.id">
                    <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" alt="">
                    <p>
                        <strong>
                            <router-link :to="{ name: 'profile', params: { id: reqUser.id } }">{{ reqUser.name }}</router-link>
                        </strong>
                    </p>
                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">182 arkadaş</p>
                        <p class="text-xs text-gray-500">120 post</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow />
            <Trends />
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const user = ref({})
const friends = ref([])
const requests = ref([])  // Burada değişken ismi requests

const getFriends = () => {
    axios.get(`/api/friends/${route.params.id}/`)
        .then(response => {
            console.log('data', response.data)
            friends.value = response.data.friends
            requests.value = response.data.requests  // Backend ile uyumlu isim burada
            user.value = response.data.user
        })
        .catch(error => {
            console.log('error', error)
        })
}

onMounted(() => {
    getFriends()
})
</script>
