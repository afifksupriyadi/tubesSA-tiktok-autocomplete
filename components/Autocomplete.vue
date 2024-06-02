<template>
  <div class="autocomplete-container mx-auto w-full max-w-lg mt-4">
    <div class="text-center mb-4">
      <h1 class="text-lg font-semibold text-gray-800 mb-1">Tugas Besar Strategi Algoritma</h1>
      <h1 class="text-lg font-semibold text-gray-800">Kelompok 3 - IF 46 07</h1>
      <hr class="border-t border-gray-300 mt-2"/>
    </div>
    <div class="relative w-full">
      <input
        type="text"
        v-model="query"
        @input="onInput"
        @keydown.enter="handleEnter"
        @keydown.up="handleArrowUp"
        @keydown.down="handleArrowDown"
        placeholder="Type to search"
        class="w-full px-4 py-2 border rounded-full bg-gray-200 text-gray-700 placeholder-gray-500 focus:outline-none focus:bg-white"
      />
      <div class="absolute inset-y-0 right-0 flex items-center pr-5">
        <span class="border-l border-gray-400 h-5 mx-2"></span>
        <Icon name="ic:outline-search" class="text-gray-500 text-2xl"/>
      </div>
    </div>
    <ul ref="suggestionsList" v-if="suggestions.length" class="border rounded mt-1 max-h-40 overflow-y-auto">
      <li
        v-for="(suggestion, index) in suggestions"
        :key="index"
        :class="{'bg-gray-200': index === selectedIndex, 'bg-white': index !== selectedIndex}"
        @click="selectSuggestion(suggestion)"
        class="cursor-pointer px-2 py-1 hover:bg-gray-300"
      >
        {{ suggestion["Track Name"] }} - {{ suggestion["Artist Name(s)"] }}
      </li>
    </ul>
    <div v-if="searchPattern || selectedText" class="mt-2">
      <div v-if="searchPattern" class="bg-blue-100 border border-blue-300 rounded-lg p-2 mb-2">
        <p class="text-xs text-blue-700">Input Pattern: <span class="font-semibold">{{ searchPattern }}</span></p>
      </div>
      <div v-if="selectedText && !notFound" class="bg-green-100 border border-green-300 rounded-lg p-2">
        <p class="text-xs text-green-700">Selected Word: <span class="font-semibold">{{ selectedText }}</span></p>
      </div>
      <div v-if="notFound" class="bg-red-100 border border-red-300 rounded-lg p-2">
        <p class="text-xs text-red-700">Selected Word: <span class="font-semibold">"Not Found"</span></p>
      </div>
    </div>
    <div v-if="selectedText || notFound" class="mt-4">
      <h3 class="text-base font-semibold">Running Time Result:</h3>
      <div class="flex justify-around mt-2">
        <div class="bg-gray-100 border border-gray-300 rounded-lg p-2 w-1/2 mx-1">
          <h4 class="text-center font-semibold mb-1">KMP</h4>
          <div class="bg-white p-2 rounded shadow">
            <p class="text-center text-xs">{{ notFound ? '0.0000000000' : kmpTime.toFixed(10) }} ms</p>
          </div>
        </div>
        <div class="bg-gray-100 border border-gray-300 rounded-lg p-2 w-1/2 mx-1">
          <h4 class="text-center font-semibold mb-1">Brute Force</h4>
          <div class="bg-white p-2 rounded shadow">
            <p class="text-center text-xs">{{ notFound ? '0.0000000000' : bruteForceTime.toFixed(10) }} ms</p>
          </div>
        </div>
      </div>
      <h3 class="text-base font-semibold mt-4">Running Time Comparison:</h3>
      <div class="flex justify-around mt-2">
        <div :class="['running-time-box', comparisonResult.bgClass]" class="border rounded-lg p-2 w-1/2 mx-1">
          <p :class="comparisonResult.textClass">
            {{ comparisonResult.message }}
          </p>
        </div>
      </div>
    </div>
    <div v-if="selectedMusic" class="mt-4">
      <h3 class="text-base font-semibold">Selected Music:</h3>
      <div class="flex items-center mt-2">
        <img :src="selectedMusic['Album Image URL']" alt="Album Cover" class="w-16 h-16 mr-4">
        <div>
          <p class="text-lg font-semibold">{{ selectedMusic['Track Name'] }}</p>
          <p class="text-md">{{ selectedMusic['Artist Name(s)'] }}</p>
        </div>
      </div>
      <audio :src="selectedMusic['Track Preview URL']" controls class="mt-4 w-full"></audio>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'
import { Icon } from '@iconify/vue'

const query = ref('')
const suggestions = ref([])
const selectedIndex = ref(-1)
const selectedText = ref('')
const kmpTime = ref(0)
const bruteForceTime = ref(0)
const searchPattern = ref('')
const comparisonResult = ref(null)
const notFound = ref(false)
const suggestionsList = ref(null)
const selectedMusic = ref(null)

const onInput = async () => {
  searchPattern.value = query.value
  if (query.value.length > 0) {
    const response = await fetch(`/api/autocomplete?q=${query.value}`)
    const data = await response.json()
    suggestions.value = data
    selectedIndex.value = -1
  } else {
    suggestions.value = []
    selectedIndex.value = -1
  }
}

const handleEnter = () => {
  if (suggestions.value.length === 0) {
    selectSuggestion(null)
  } else if (selectedIndex.value !== -1) {
    selectSuggestion(suggestions.value[selectedIndex.value])
  } else {
    selectSuggestion(null)
  }
}

const handleArrowUp = async (event) => {
  if (selectedIndex.value > 0) {
    selectedIndex.value -= 1
  } else {
    selectedIndex.value = suggestions.value.length - 1
  }
  await nextTick()
  scrollToSelectedItem()
}

const handleArrowDown = async (event) => {
  if (selectedIndex.value < suggestions.value.length - 1) {
    selectedIndex.value += 1
  } else {
    selectedIndex.value = 0
  }
  await nextTick()
  scrollToSelectedItem()
}

const scrollToSelectedItem = () => {
  if (suggestionsList.value && selectedIndex.value !== -1) {
    const selectedItem = suggestionsList.value.children[selectedIndex.value]
    if (selectedItem) {
      selectedItem.scrollIntoView({ block: 'nearest', behavior: 'smooth' })
    }
  }
}

const selectSuggestion = async (suggestion) => {
  if (suggestion) {
    selectedText.value = `${suggestion['Track Name']} - ${suggestion['Artist Name(s)']}`
    notFound.value = false
    selectedMusic.value = suggestion
  } else {
    selectedText.value = 'Not Found'
    notFound.value = true
    kmpTime.value = 0
    bruteForceTime.value = 0
    selectedMusic.value = null
    calculateComparisonResult()
    return
  }

  suggestions.value = []

  const response = await fetch(`/api/compare`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: suggestion['Track Name'],
      pattern: searchPattern.value,
    }),
  })
  const data = await response.json()
  kmpTime.value = data.kmp_time
  bruteForceTime.value = data.brute_force_time
  query.value = `${suggestion['Track Name']} - ${suggestion['Artist Name(s)']}`

  calculateComparisonResult()
}

const calculateComparisonResult = () => {
  const difference = (Math.abs(kmpTime.value - bruteForceTime.value)).toFixed(10)
  if (notFound.value) {
    comparisonResult.value = {
      message: `Input pattern not found in database.`,
      bgClass: 'bg-yellow-100 border-yellow-300',
      textClass: 'text-yellow-700'
    }
  } else if (kmpTime.value < bruteForceTime.value) {
    comparisonResult.value = {
      message: `KMP is ${difference} ms faster than Brute Force.`,
      bgClass: 'bg-green-100 border-green-300',
      textClass: 'text-green-700'
    }
  } else if (kmpTime.value > bruteForceTime.value) {
    comparisonResult.value = {
      message: `Brute Force is ${difference} ms faster than KMP.`,
      bgClass: 'bg-red-100 border-red-300',
      textClass: 'text-red-700'
    }
  } else {
    comparisonResult.value = {
      message: `Both algorithms have the same running time.`,
      bgClass: 'bg-yellow-100 border-yellow-300',
      textClass: 'text-yellow-700'
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 500px;
}
.bg-gray-200 {
  background-color: #edf2f7;
}
.bg-white {
  background-color: #ffffff;
}
.autocomplete-container {
  max-width: 500px;
  margin: 0 auto;
}
.running-time-box {
  font-size: 0.75rem; /* Perkecil ukuran teks */
  padding: 0.5rem; /* Perkecil ukuran background */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Tambahkan shadow */
  border-radius: 0.375rem; /* Rounded corners */
}
.running-time-box p {
  margin: 0;
  padding: 0;
}
</style>
