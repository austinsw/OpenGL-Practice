#version 330 core

in vec2 uv_0;

out vec4 fragColor;

void main() {
    vec3 color = vec3(uv_0, 0);
    fragColor = vec4(color, 1.0);
}