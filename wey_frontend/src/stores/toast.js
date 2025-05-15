// src/stores/toast.js
import { defineStore } from 'pinia'

export const useToastStore = defineStore('toast',{
    id: 'toast',
    state: () => ({
        ms: 0,
        message: '',
        classes: [],
        isVisible: false
    }),
    actions: {
        showToast(ms, message, classes) {
            this.ms = parseInt(ms)
            this.message = message
            this.classes = classes
            this.isVisible = true
            setTimeout(() => {
                this.classes.push('-translate-y-28')
            }, 10)
            setTimeout(() => {
                this.classes = this.classes.filter(cls => cls !== '-translate-y-28')
            }, this.ms - 500)
            setTimeout(() => {
                this.isVisible = false
            }, this.ms)
        }
    }
})
