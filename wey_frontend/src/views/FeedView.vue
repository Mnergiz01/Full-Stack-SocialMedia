<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
       
        <div class="main-center col-span-3 space-y-4">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
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
import { onMounted, ref } from 'vue'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '@/components/FeedItem.vue'

const posts = ref([])
const body = ref('')

onMounted(() => {
    getFeed()
})

const getFeed = () => {
    axios.get('/api/posts/').then(response => {
        console.log('data', response.data)
        posts.value = response.data
    })
        .catch(error => {
            console.log('error', error)
        })
}
const submitForm = () => {
    console.log('submitForm :', body.value);
    axios
    .post('/api/posts/create/',{
        'body':body.value
    })
    .then(response => {
        console.log('data',response.data);
        posts.value.unshift(response.data)
        body.value=''
    })
    .catch(error => {
            console.log('error', error)
        })
}
</script>