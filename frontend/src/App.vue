<template>
  <div class="system-dashboard">
    <section class="sidebar">
      <div class="sidebar-head">
        <button class="opener-elements system-button" v-if="!selectedElement">Elements</button>
        <button class="opener-elements system-button" v-else @click="deselectElement">Back</button>
      </div>
      <div class="elements" v-if="!selectedElement">
        <div class="element" @click="addElement('title')">
          <img src="https://cdn-icons-png.flaticon.com/512/2799/2799932.png" alt="Title" class="element-icon">
          <h3 class="element-name">Title</h3>
        </div>
        <div class="element" @click="addElement('text')">
          <img src="https://static.thenounproject.com/png/13795-200.png" alt="Text" class="element-icon">
          <h3 class="element-name">Text</h3>
        </div>
        <div class="element" @click="addElement('image')">
          <img src="https://cdn-icons-png.flaticon.com/512/25/25666.png" alt="Image" class="element-icon">
          <h3 class="element-name">Image</h3>
        </div>
        <div class="element" @click="addElement('button')">
          <img src="https://cdn-icons-png.flaticon.com/512/3305/3305815.png" alt="Button" class="element-icon">
          <h3 class="element-name">Button</h3>
        </div>
      </div>
      <div class="element-settings" v-if="selectedElement">
        <h3>Element Settings</h3>

        <!-- Настройки для Title -->
        <div v-if="selectedElement.props.tag === 'h1'">
          <label>Content:</label>
          <input v-model="selectedElement.props.content" type="text" />

          <label>Tag:</label>
          <select v-model="selectedElement.props.tag">
            <option value="h1">H1</option>
            <option value="h2">H2</option>
            <option value="h3">H3</option>
            <option value="h4">H4</option>
            <option value="h5">H5</option>
            <option value="h6">H6</option>
          </select>

          <label>Color:</label>
          <input type="color" v-model="selectedElement.props.color" />

          <label>Text Align:</label>
          <select v-model="selectedElement.props.textAlign">
            <option value="text-left">Left</option>
            <option value="text-center">Center</option>
            <option value="text-right">Right</option>
          </select>

          <label>Font Family:</label>
          <select v-model="selectedElement.props.fontFamily">
            <option value="font-sans">Sans</option>
            <option value="font-serif">Serif</option>
            <option value="font-mono">Monospace</option>
          </select>

          <label>Font Size:</label>
          <select v-model="selectedElement.props.fontSize">
            <option value="text-sm">Small</option>
            <option value="text-base">Base</option>
            <option value="text-lg">Large</option>
            <option value="text-xl">Extra Large</option>
          </select>

          <label>Font Weight:</label>
          <select v-model="selectedElement.props.fontWeight">
            <option value="font-thin">Thin</option>
            <option value="font-normal">Normal</option>
            <option value="font-bold">Bold</option>
          </select>

          <label>Line Height:</label>
          <select v-model="selectedElement.props.lineHeight">
            <option value="leading-none">None</option>
            <option value="leading-tight">Tight</option>
            <option value="leading-normal">Normal</option>
            <option value="leading-loose">Loose</option>
          </select>

          <label>Margin:</label>
          <select v-model="selectedElement.props.margin">
            <option value="m-0">0</option>
            <option value="m-2">2</option>
            <option value="m-4">4</option>
            <option value="m-8">8</option>
          </select>

          <label>Padding:</label>
          <select v-model="selectedElement.props.padding">
            <option value="p-0">0</option>
            <option value="p-2">2</option>
            <option value="p-4">4</option>
            <option value="p-8">8</option>
          </select>
        </div>

        <!-- Настройки для Text -->
        <div v-if="selectedElement.props.tag === 'p'">
          <label>Text Content:</label>
          <input v-model="selectedElement.props.content" type="text" />

          <label>Align:</label>
          <select v-model="selectedElement.props.textAlign">
            <option value="text-left">Left</option>
            <option value="text-center">Center</option>
            <option value="text-right">Right</option>
          </select>

          <label>Color:</label>
          <input type="color" v-model="selectedElement.props.color" />

          <label>Font Family:</label>
          <select v-model="selectedElement.props.fontFamily">
            <option value="font-sans">Sans</option>
            <option value="font-serif">Serif</option>
            <option value="font-mono">Monospace</option>
          </select>

          <label>Font Size:</label>
          <select v-model="selectedElement.props.fontSize">
            <option value="text-sm">Small</option>
            <option value="text-base">Base</option>
            <option value="text-lg">Large</option>
            <option value="text-xl">Extra Large</option>
          </select>

          <label>Font Weight:</label>
          <select v-model="selectedElement.props.fontWeight">
            <option value="font-thin">Thin</option>
            <option value="font-normal">Normal</option>
            <option value="font-bold">Bold</option>
          </select>

          <label>Line Height:</label>
          <select v-model="selectedElement.props.lineHeight">
            <option value="leading-none">None</option>
            <option value="leading-tight">Tight</option>
            <option value="leading-normal">Normal</option>
            <option value="leading-loose">Loose</option>
          </select>

          <label>Margin:</label>
          <select v-model="selectedElement.props.margin">
            <option value="m-0">0</option>
            <option value="m-2">2</option>
            <option value="m-4">4</option>
            <option value="m-8">8</option>
          </select>

          <label>Padding:</label>
          <select v-model="selectedElement.props.padding">
            <option value="p-0">0</option>
            <option value="p-2">2</option>
            <option value="p-4">4</option>
            <option value="p-8">8</option>
          </select>
        </div>

        <!-- Настройки для Image -->
        <div v-if="selectedElement.props.tag === 'img'">
          <label>Image Source:</label>
          <input v-model="selectedElement.props.src" type="text" />

          <label>Alt Text:</label>
          <input v-model="selectedElement.props.alt" type="text" />

          <label>Align:</label>
          <select v-model="selectedElement.props.textAlign">
            <option value="text-left">Left</option>
            <option value="text-center">Center</option>
            <option value="text-right">Right</option>
          </select>

          <label>Width:</label>
          <input v-model="selectedElement.props.width" type="number" />

          <label>Height:</label>
          <input v-model="selectedElement.props.height" type="number" />
        </div>

        <!-- Настройки для Button -->
        <div v-if="selectedElement.props.tag === 'button'">
          <label>Button Text:</label>
          <input v-model="selectedElement.props.content" type="text" />

          <label>Link (href):</label>
          <input v-model="selectedElement.props.href" type="text" />

          <label>Align:</label>
          <select v-model="selectedElement.props.textAlign">
            <option value="text-left">Left</option>
            <option value="text-center">Center</option>
            <option value="text-right">Right</option>
          </select>

          <label>Text Color:</label>
          <input type="color" v-model="selectedElement.props.color" />

          <label>Background Color:</label>
          <input type="color" v-model="selectedElement.props.backgroundColor" />

          <label>Border Type:</label>
          <select v-model="selectedElement.props.borderType">
            <option value="solid">Solid</option>
            <option value="dashed">Dashed</option>
            <option value="dotted">Dotted</option>
          </select>

          <label>Border Radius:</label>
          <input v-model="selectedElement.props.borderRadius" type="number" />

          <label>Border Color:</label>
          <input type="color" v-model="selectedElement.props.borderColor" />

          <label>Margin:</label>
          <select v-model="selectedElement.props.margin">
            <option value="m-0">0</option>
            <option value="m-2">2</option>
            <option value="m-4">4</option>
            <option value="m-8">8</option>
          </select>

          <label>Padding:</label>
          <select v-model="selectedElement.props.padding">
            <option value="p-0">0</option>
            <option value="p-2">2</option>
            <option value="p-4">4</option>
            <option value="p-8">8</option>
          </select>
        </div>

        <button class="delete-element system-button" @click="deleteElement">Delete Element</button>
      </div>
    </section>

    <section class="board">
      <div class="page">
        <component 
          v-for="(element, index) in pageElements" 
          :is="element.props.tag" 
          :key="element.id" 
          :class="[element.props.color, element.props.textAlign, element.props.fontFamily, element.props.fontSize, element.props.fontWeight, element.props.lineHeight, element.props.margin, element.props.padding]" 
          :src="element.props.src" 
          :alt="element.props.alt" 
          :style="{ backgroundColor: element.props.backgroundColor, borderRadius: element.props.borderRadius + 'px', borderColor: element.props.borderColor, borderStyle: element.props.borderType, width: element.props.width + 'px', height: element.props.height + 'px' }"
          @click="selectElement(element, $event)"
        >
          {{ element.props.content }}
        </component>
      </div>
      <div class="add-element-button">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR74Hj8swURNBBKwqS6Nj7dypcf-a3q4amYag&s" alt="" class="add-element-button-icon">
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';

export default defineComponent({
  name: 'SiteBuilder',
  setup() {
    const pageElements = ref<any[]>([]);
    const selectedElementId = ref<number | null>(null);

    const elementMap: Record<string, any> = {
      title: { props: { tag: 'h1', content: 'Заголовок по умолчанию' } },
      text: { props: { tag: 'p', content: 'Текст по умолчанию' } },
      image: { props: { tag: 'img', src: 'https://via.placeholder.com/150', alt: 'Example Image', width: 150, height: 150 } },
      button: { props: { tag: 'button', content: 'Кнопка', backgroundColor: '#ffffff', borderColor: '#000000', borderType: 'solid', borderRadius: 0, href: '#' } },
    };

    const addElement = (type: string) => {
      const newElement = {
        ...elementMap[type], 
        props: { ...elementMap[type].props }, // Глубокое копирование props
        id: Date.now() 
      };
      pageElements.value.push(newElement);
    };

    const selectElement = (element: any, event: MouseEvent) => {
      event.stopPropagation();
      selectedElementId.value = element.id;
    };

    const deselectElement = () => {
      selectedElementId.value = null;
    };

    const deleteElement = () => {
      pageElements.value = pageElements.value.filter(el => el.id !== selectedElementId.value);
      deselectElement();
    };

    const selectedElement = computed(() => pageElements.value.find(el => el.id === selectedElementId.value) || null);

    return { pageElements, selectedElement, addElement, selectElement, deselectElement, deleteElement };
  },
});
</script>

<style scoped>
.system-dashboard {
  display: flex;
}

.sidebar {
  width: 250px;
  background-color: #f4f4f9;
}

.board {
  flex-grow: 1;
  background-color: #fff;
  padding: 20px;
}

.page {
  min-height: 400px;
  border: 2px dashed #ccc;
}

.element-settings input, .element-settings select {
  width: 100%;
  margin-bottom: 10px;
}
</style>




<!-- <script setup lang="ts">
</script>

<template>
  <div class="system-dashboard">
  <section class="sidebar">
    <div class="sidebar-head">
      <button class="opener-elements system-button">Elements</button>
    </div>
    <div class="elements">
      <div class="element">
        <img src="https://cdn-icons-png.flaticon.com/512/2799/2799932.png" alt="Title" class="element-icon">
        <h3 class="element-name">Title</h3>
      </div>
      <div class="element">
        <img src="https://static.thenounproject.com/png/13795-200.png" alt="Text" class="element-icon">
        <h3 class="element-name">Text</h3>
      </div>
      <div class="element">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25666.png" alt="Image" class="element-icon">
        <h3 class="element-name">Image</h3>
      </div>
      <div class="element">
        <img src="https://cdn-icons-png.flaticon.com/512/3305/3305815.png" alt="Button" class="element-icon">
        <h3 class="element-name">Button</h3>
      </div>
    </div>
    <div class="sidebar-footer">
      <button class="update-elements system-button">Save</button>
      <button class="generate-elements system-button">Generate</button>
    </div>
  </section>

  <section class="board">
    <div class="page">

    </div>
    <div class="add-element-button">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR74Hj8swURNBBKwqS6Nj7dypcf-a3q4amYag&s" alt="" class="add-element-button-icon">
    </div>
  </section>
  </div>
</template> -->
