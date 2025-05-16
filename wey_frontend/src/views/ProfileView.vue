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
                        182 Arkadaş
                    </router-link>
                    <p class="text-xs text-gray-500">120 Post</p>
                </div>
                <div class="mt-6">
                    <button class="inline-block py-4 px-3 bg-purple-600 text-xs text-white rounded-lg"
                        @click="sendFriendshipRequest">Arkadaşlık İsteği Gönder</button>
                </div>
            </div>
        </div>
        <div class="main-center col-span-2 space-y-4">
            <div class="p-4 bg-white border border-gray-200 rounded-lg" v-if="userStore.id === user.id">
                <form method="post" @submit.prevent="submitForm">
                    <div class="p-4">
                        <textarea class="p-4 w-full bg-gray-100 rounded-lg"
                            placeholder="Paylaşım Yapmak İster Misiniz ? " v-model="body"></textarea>
                    </div>
                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <a href="#"
                            class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg hover:bg-gray-900 transation duration-300">Fotoğraf
                            Ekle</a>
                        <button href="#"
                            class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg hover:bg-purple-900 transation duration-300">Post</button>
                    </div>
                </form>
            </div>



            <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" :key="post.id">
                <FeedItem :post="post"></FeedItem>
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
import { onMounted, onUpdated, ref, watch } from 'vue'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import { useUserStore } from '@/stores/user'
import { useRoute } from 'vue-router'
import FeedItem from '@/components/FeedItem.vue'

const route = useRoute()


const userStore = useUserStore()
const posts = ref([])
const body = ref('')
const user = ref({})

onMounted(() => {
    getFeed()
})
// route.params.id değiştiğinde yeniden veri çek
watch(() => route.params.id, (newId, oldId) => {
    if (newId !== oldId) {
        getFeed()
    }
})
onUpdated(() => {
    // getFeed()
})

const getFeed = () => {
    axios.get(`/api/posts/profile/${route.params.id}/`).then(response => {
        console.log('data', response.data)
        posts.value = response.data.posts
        user.value = response.data.user
    })
        .catch(error => {
            console.log('error', error)
        })
}


const submitForm = () => {
    console.log('submitForm :', body.value);
    axios
        .post('/api/posts/create/', {
            'body': body.value
        })
        .then(response => {
            console.log('data', response.data);
            posts.value.unshift(response.data)
            body.value = ''
        })
        .catch(error => {
            console.log('error', error)
        })
}
const sendFriendshipRequest = () => {
    axios.post(`/api/friends/${route.params.id}/request/`)
        .then(response => {
            console.log('data', response.data)

        })
        .catch(error => {
            console.log('error', error);
        })
}
</script>