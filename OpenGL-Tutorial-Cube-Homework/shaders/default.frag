#version 330 core

//in vec2 uv_0;
in vec3 vertex_color;

out vec4 fragColor;

void main() {
    //vec3 color = vec3(uv_0, 0);
    vec3 color = vec3(vertex_color);
    fragColor = vec4(color, 1.0);
}