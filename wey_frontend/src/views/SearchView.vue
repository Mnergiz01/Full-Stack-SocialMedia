<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-3 space-y-4 ">
            <div class="bg-white border border-gray-200 rounded-lg">
                <form @submit.prevent="submitForm" class="p-2 flex space-x-4">
                    <input v-model="query" type="search" class="p-4 w-full bg-grat-100 rounded-lg"
                        placeholder="Arama Yapmak İçin Tıklayınız.">
                    <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">ara</button>
                </form>
            </div>
            <div class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4" v-if="users.length">
                <div class="p-4 bg-white border border-gray-200 text-center rounded-lg" v-for="user in users"
                    :key="user.id">
                    <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" alt="">
                    <p>
                        <strong>
                            <router-link :to="{ name: 'profile', params: { 'id': user.id } }">{{ user.name }}</router-link>
                        </strong>
                    </p>
                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">182 arkadaş</p>
                        <p class="text-xs text-gray-500">120 post</p>
                    </div>
                </div>
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
import { ref } from 'vue'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '@/components/FeedItem.vue'

const query = ref('')
const users = ref([])
const posts = ref([])

const submitForm = () => {
    axios
        .post('/api/search/', {
            query: query.value
        })
        .then(response => {
            console.log('response :', response.data);
            users.value = response.data.users
            posts.value = response.data.posts
        })
        .catch(error => {
            console.log('error :', error);
        })

}
</script>