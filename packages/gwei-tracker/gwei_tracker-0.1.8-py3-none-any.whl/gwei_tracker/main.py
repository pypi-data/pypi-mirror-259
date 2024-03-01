from pathlib import Path
import playwright.async_api as playwright
from etherscan import Etherscan
from time import strftime

txt1 = """<html lang="en">
   <head>
      <meta charset="utf-8">
      <style>@import url(https://fonts.googleapis.com/css2?family=Roboto&display=swap); /*
         ! tailwindcss v3.1.8 | MIT License | https://tailwindcss.com
         */
         *,:after,:before {
         border: 0 solid #e5e7eb;
         box-sizing: border-box
         }
         :after,:before {
         --tw-content: ""
         }
         html {
         -webkit-text-size-adjust: 100%;
         font-family: ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;
         line-height: 1.5;
         tab-size: 4
         }
         body {
         line-height: inherit;
         margin: 0
         }
         hr {
         border-top-width: 1px;
         color: inherit;
         height: 0
         }
         abbr:where([title]) {
         -webkit-text-decoration: underline dotted;
         text-decoration: underline dotted
         }
         h1,h2,h3,h4,h5,h6 {
         font-size: inherit;
         font-weight: inherit
         }
         a {
         color: inherit;
         text-decoration: inherit
         }
         b,strong {
         font-weight: bolder
         }
         code,kbd,pre,samp {
         font-family: ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace;
         font-size: 1em
         }
         small {
         font-size: 80%
         }
         sub,sup {
         font-size: 75%;
         line-height: 0;
         position: relative;
         vertical-align: initial
         }
         sub {
         bottom: -.25em
         }
         sup {
         top: -.5em
         }
         table {
         border-collapse: collapse;
         border-color: inherit;
         text-indent: 0
         }
         button,input,optgroup,select,textarea {
         color: inherit;
         font-family: inherit;
         font-size: 100%;
         font-weight: inherit;
         line-height: inherit;
         margin: 0;
         padding: 0
         }
         button,select {
         text-transform: none
         }
         [type=button],[type=reset],[type=submit],button {
         -webkit-appearance: button;
         background-color: initial;
         background-image: none
         }
         :-moz-focusring {
         outline: auto
         }
         :-moz-ui-invalid {
         box-shadow: none
         }
         progress {
         vertical-align: initial
         }
         ::-webkit-inner-spin-button,::-webkit-outer-spin-button {
         height: auto
         }
         [type=search] {
         -webkit-appearance: textfield;
         outline-offset: -2px
         }
         ::-webkit-search-decoration {
         -webkit-appearance: none
         }
         ::-webkit-file-upload-button {
         -webkit-appearance: button;
         font: inherit
         }
         summary {
         display: list-item
         }
         blockquote,dd,dl,figure,h1,h2,h3,h4,h5,h6,hr,p,pre {
         margin: 0
         }
         fieldset {
         margin: 0
         }
         fieldset,legend {
         padding: 0
         }
         menu,ol,ul {
         list-style: none;
         margin: 0;
         padding: 0
         }
         textarea {
         resize: vertical
         }
         input::-webkit-input-placeholder,textarea::-webkit-input-placeholder {
         color: #9ca3af
         }
         input::placeholder,textarea::placeholder {
         color: #9ca3af
         }
         [role=button],button {
         cursor: pointer
         }
         :disabled {
         cursor: default
         }
         audio,canvas,embed,iframe,img,object,svg,video {
         display: block;
         vertical-align: middle
         }
         img,video {
         height: auto;
         max-width: 100%
         }
         [multiple],[type=date],[type=datetime-local],[type=email],[type=month],[type=number],[type=password],[type=search],[type=tel],[type=text],[type=time],[type=url],[type=week],select,textarea {
         --tw-shadow: 0 0 #0000;
         -webkit-appearance: none;
         appearance: none;
         background-color: #fff;
         border-color: #6b7280;
         border-radius: 0;
         border-width: 1px;
         font-size: 1rem;
         line-height: 1.5rem;
         padding: .5rem .75rem
         }
         [multiple]:focus,[type=date]:focus,[type=datetime-local]:focus,[type=email]:focus,[type=month]:focus,[type=number]:focus,[type=password]:focus,[type=search]:focus,[type=tel]:focus,[type=text]:focus,[type=time]:focus,[type=url]:focus,[type=week]:focus,select:focus,textarea:focus {
         --tw-ring-inset: var(--tw-empty,/*!*/ /*!*/);
         --tw-ring-offset-width: 0px;
         --tw-ring-offset-color: #fff;
         --tw-ring-color: #2563eb;
         --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
         --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(1px + var(--tw-ring-offset-width)) var(--tw-ring-color);
         border-color: #2563eb;
         box-shadow: var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow);
         outline: 2px solid transparent;
         outline-offset: 2px
         }
         input::-webkit-input-placeholder,textarea::-webkit-input-placeholder {
         color: #6b7280;
         opacity: 1
         }
         input::placeholder,textarea::placeholder {
         color: #6b7280;
         opacity: 1
         }
         ::-webkit-datetime-edit-fields-wrapper {
         padding: 0
         }
         ::-webkit-date-and-time-value {
         min-height: 1.5em
         }
         ::-webkit-datetime-edit,::-webkit-datetime-edit-day-field,::-webkit-datetime-edit-hour-field,::-webkit-datetime-edit-meridiem-field,::-webkit-datetime-edit-millisecond-field,::-webkit-datetime-edit-minute-field,::-webkit-datetime-edit-month-field,::-webkit-datetime-edit-second-field,::-webkit-datetime-edit-year-field {
         padding-bottom: 0;
         padding-top: 0
         }
         select {
         background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3E%3Cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='m6 8 4 4 4-4'/%3E%3C/svg%3E");
         background-position: right .5rem center;
         background-repeat: no-repeat;
         background-size: 1.5em 1.5em;
         padding-right: 2.5rem;
         -webkit-print-color-adjust: exact;
         print-color-adjust: exact
         }
         [multiple] {
         background-image: none;
         background-position: 0 0;
         background-repeat: repeat;
         background-size: initial;
         padding-right: .75rem;
         -webkit-print-color-adjust: inherit;
         print-color-adjust: inherit
         }
         [type=checkbox],[type=radio] {
         --tw-shadow: 0 0 #0000;
         -webkit-appearance: none;
         appearance: none;
         background-color: #fff;
         background-origin: border-box;
         border-color: #6b7280;
         border-width: 1px;
         color: #2563eb;
         display: inline-block;
         flex-shrink: 0;
         height: 1rem;
         padding: 0;
         -webkit-print-color-adjust: exact;
         print-color-adjust: exact;
         -webkit-user-select: none;
         user-select: none;
         vertical-align: middle;
         width: 1rem
         }
         [type=checkbox] {
         border-radius: 0
         }
         [type=radio] {
         border-radius: 100%
         }
         [type=checkbox]:focus,[type=radio]:focus {
         --tw-ring-inset: var(--tw-empty,/*!*/ /*!*/);
         --tw-ring-offset-width: 2px;
         --tw-ring-offset-color: #fff;
         --tw-ring-color: #2563eb;
         --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
         --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color);
         box-shadow: var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow);
         outline: 2px solid transparent;
         outline-offset: 2px
         }
         [type=checkbox]:checked,[type=radio]:checked {
         background-color: currentColor;
         background-position: 50%;
         background-repeat: no-repeat;
         background-size: 100% 100%;
         border-color: transparent
         }
         [type=checkbox]:checked {
         background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg viewBox='0 0 16 16' fill='%23fff' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M12.207 4.793a1 1 0 0 1 0 1.414l-5 5a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L6.5 9.086l4.293-4.293a1 1 0 0 1 1.414 0z'/%3E%3C/svg%3E")
         }
         [type=radio]:checked {
         background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg viewBox='0 0 16 16' fill='%23fff' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='8' cy='8' r='3'/%3E%3C/svg%3E")
         }
         [type=checkbox]:checked:focus,[type=checkbox]:checked:hover,[type=radio]:checked:focus,[type=radio]:checked:hover {
         background-color: currentColor;
         border-color: transparent
         }
         [type=checkbox]:indeterminate {
         background-color: currentColor;
         background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 16 16'%3E%3Cpath stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M4 8h8'/%3E%3C/svg%3E");
         background-position: 50%;
         background-repeat: no-repeat;
         background-size: 100% 100%;
         border-color: transparent
         }
         [type=checkbox]:indeterminate:focus,[type=checkbox]:indeterminate:hover {
         background-color: currentColor;
         border-color: transparent
         }
         [type=file] {
         background: transparent none repeat 0 0/auto auto padding-box border-box scroll;
         background: initial;
         border-color: inherit;
         border-radius: 0;
         border-width: 0;
         font-size: inherit;
         line-height: inherit;
         padding: 0
         }
         [type=file]:focus {
         outline: 1px solid ButtonText;
         outline: 1px auto -webkit-focus-ring-color
         }
         html {
         font-family: Roboto,sans-serif
         }
         *,:after,:before {
         --tw-border-spacing-x: 0;
         --tw-border-spacing-y: 0;
         --tw-translate-x: 0;
         --tw-translate-y: 0;
         --tw-rotate: 0;
         --tw-skew-x: 0;
         --tw-skew-y: 0;
         --tw-scale-x: 1;
         --tw-scale-y: 1;
         --tw-pan-x: ;
         --tw-pan-y: ;
         --tw-pinch-zoom: ;
         --tw-scroll-snap-strictness: proximity;
         --tw-ordinal: ;
         --tw-slashed-zero: ;
         --tw-numeric-figure: ;
         --tw-numeric-spacing: ;
         --tw-numeric-fraction: ;
         --tw-ring-inset: ;
         --tw-ring-offset-width: 0px;
         --tw-ring-offset-color: #fff;
         --tw-ring-color: rgba(59,130,246,.5);
         --tw-ring-offset-shadow: 0 0 #0000;
         --tw-ring-shadow: 0 0 #0000;
         --tw-shadow: 0 0 #0000;
         --tw-shadow-colored: 0 0 #0000;
         --tw-blur: ;
         --tw-brightness: ;
         --tw-contrast: ;
         --tw-grayscale: ;
         --tw-hue-rotate: ;
         --tw-invert: ;
         --tw-saturate: ;
         --tw-sepia: ;
         --tw-drop-shadow: ;
         --tw-backdrop-blur: ;
         --tw-backdrop-brightness: ;
         --tw-backdrop-contrast: ;
         --tw-backdrop-grayscale: ;
         --tw-backdrop-hue-rotate: ;
         --tw-backdrop-invert: ;
         --tw-backdrop-opacity: ;
         --tw-backdrop-saturate: ;
         --tw-backdrop-sepia:
         }
         ::-webkit-backdrop {
         --tw-border-spacing-x: 0;
         --tw-border-spacing-y: 0;
         --tw-translate-x: 0;
         --tw-translate-y: 0;
         --tw-rotate: 0;
         --tw-skew-x: 0;
         --tw-skew-y: 0;
         --tw-scale-x: 1;
         --tw-scale-y: 1;
         --tw-pan-x: ;
         --tw-pan-y: ;
         --tw-pinch-zoom: ;
         --tw-scroll-snap-strictness: proximity;
         --tw-ordinal: ;
         --tw-slashed-zero: ;
         --tw-numeric-figure: ;
         --tw-numeric-spacing: ;
         --tw-numeric-fraction: ;
         --tw-ring-inset: ;
         --tw-ring-offset-width: 0px;
         --tw-ring-offset-color: #fff;
         --tw-ring-color: rgba(59,130,246,.5);
         --tw-ring-offset-shadow: 0 0 #0000;
         --tw-ring-shadow: 0 0 #0000;
         --tw-shadow: 0 0 #0000;
         --tw-shadow-colored: 0 0 #0000;
         --tw-blur: ;
         --tw-brightness: ;
         --tw-contrast: ;
         --tw-grayscale: ;
         --tw-hue-rotate: ;
         --tw-invert: ;
         --tw-saturate: ;
         --tw-sepia: ;
         --tw-drop-shadow: ;
         --tw-backdrop-blur: ;
         --tw-backdrop-brightness: ;
         --tw-backdrop-contrast: ;
         --tw-backdrop-grayscale: ;
         --tw-backdrop-hue-rotate: ;
         --tw-backdrop-invert: ;
         --tw-backdrop-opacity: ;
         --tw-backdrop-saturate: ;
         --tw-backdrop-sepia:
         }
         ::backdrop {
         --tw-border-spacing-x: 0;
         --tw-border-spacing-y: 0;
         --tw-translate-x: 0;
         --tw-translate-y: 0;
         --tw-rotate: 0;
         --tw-skew-x: 0;
         --tw-skew-y: 0;
         --tw-scale-x: 1;
         --tw-scale-y: 1;
         --tw-pan-x: ;
         --tw-pan-y: ;
         --tw-pinch-zoom: ;
         --tw-scroll-snap-strictness: proximity;
         --tw-ordinal: ;
         --tw-slashed-zero: ;
         --tw-numeric-figure: ;
         --tw-numeric-spacing: ;
         --tw-numeric-fraction: ;
         --tw-ring-inset: ;
         --tw-ring-offset-width: 0px;
         --tw-ring-offset-color: #fff;
         --tw-ring-color: rgba(59,130,246,.5);
         --tw-ring-offset-shadow: 0 0 #0000;
         --tw-ring-shadow: 0 0 #0000;
         --tw-shadow: 0 0 #0000;
         --tw-shadow-colored: 0 0 #0000;
         --tw-blur: ;
         --tw-brightness: ;
         --tw-contrast: ;
         --tw-grayscale: ;
         --tw-hue-rotate: ;
         --tw-invert: ;
         --tw-saturate: ;
         --tw-sepia: ;
         --tw-drop-shadow: ;
         --tw-backdrop-blur: ;
         --tw-backdrop-brightness: ;
         --tw-backdrop-contrast: ;
         --tw-backdrop-grayscale: ;
         --tw-backdrop-hue-rotate: ;
         --tw-backdrop-invert: ;
         --tw-backdrop-opacity: ;
         --tw-backdrop-saturate: ;
         --tw-backdrop-sepia:
         }
         .pointer-events-none {
         pointer-events: none
         }
         .static {
         position: static
         }
         .fixed {
         position: fixed
         }
         .absolute {
         position: absolute
         }
         .inset-0 {
         bottom: 0;
         left: 0;
         right: 0;
         top: 0
         }
         .z-10 {
         z-index: 10
         }
         .z-50 {
         z-index: 50
         }
         .mx-4 {
         margin-left: 1rem;
         margin-right: 1rem
         }
         .mx-5 {
         margin-left: 1.25rem;
         margin-right: 1.25rem
         }
         .mx-2 {
         margin-left: .5rem;
         margin-right: .5rem
         }
         .mb-1 {
         margin-bottom: .25rem
         }
         .ml-1 {
         margin-left: .25rem
         }
         .ml-2 {
         margin-left: .5rem
         }
         .mt-2 {
         margin-top: .5rem
         }
         .mb-2 {
         margin-bottom: .5rem
         }
         .-ml-8 {
         margin-left: -2rem
         }
         .block {
         display: block
         }
         .flex {
         display: flex
         }
         .inline-flex {
         display: inline-flex
         }
         .table {
         display: table
         }
         .grid {
         display: grid
         }
         .hidden {
         display: none
         }
         .h-8 {
         height: 2rem
         }
         .h-7 {
         height: 1.75rem
         }
         .h-4 {
         height: 1rem
         }
         .h-\[11px\] {
         height: 11px
         }
         .h-\[17px\] {
         height: 17px
         }
         .h-9 {
         height: 2.25rem
         }
         .h-\[89px\] {
         height: 89px
         }
         .h-3 {
         height: .75rem
         }
         .min-h-\[182px\] {
         min-height: 182px
         }
         .w-4 {
         width: 1rem
         }
         .w-\[11px\] {
         width: 11px
         }
         .w-\[26px\] {
         width: 26px
         }
         .w-40 {
         width: 10rem
         }
         .w-10 {
         width: 2.5rem
         }
         .w-full {
         width: 100%
         }
         .w-\[89px\] {
         width: 89px
         }
         .w-3 {
         width: .75rem
         }
         .min-w-\[450px\] {
         min-width: 450px
         }
         .max-w-\[450px\] {
         max-width: 450px
         }
         .transform {
         -webkit-transform: translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
         transform: translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
         }
         .resize {
         resize: both
         }
         .grid-cols-3 {
         grid-template-columns: repeat(3,minmax(0,1fr))
         }
         .flex-row {
         flex-direction: row
         }
         .flex-row-reverse {
         flex-direction: row-reverse
         }
         .flex-col {
         flex-direction: column
         }
         .place-content-between {
         place-content: space-between
         }
         .items-center {
         align-items: center
         }
         .justify-center {
         justify-content: center
         }
         .justify-between {
         justify-content: space-between
         }
         .justify-around {
         justify-content: space-around
         }
         .gap-4 {
         gap: 1rem
         }
         .gap-2 {
         gap: .5rem
         }
         .space-y-4>:not([hidden])~:not([hidden]) {
         --tw-space-y-reverse: 0;
         margin-bottom: calc(1rem*var(--tw-space-y-reverse));
         margin-top: calc(1rem*(1 - var(--tw-space-y-reverse)))
         }
         .rounded-lg {
         border-radius: .5rem
         }
         .rounded-md {
         border-radius: .375rem
         }
         .rounded-full {
         border-radius: 9999px
         }
         .border {
         border-width: 1px
         }
         .border-2 {
         border-width: 2px
         }
         .border-t {
         border-top-width: 1px
         }
         .border-b {
         border-bottom-width: 1px
         }
         .border-slate-200 {
         --tw-border-opacity: 1;
         border-color: rgb(226 232 240/var(--tw-border-opacity))
         }
         .border-slate-100 {
         --tw-border-opacity: 1;
         border-color: rgb(241 245 249/var(--tw-border-opacity))
         }
         .border-transparent {
         border-color: transparent
         }
         .border-gray-200 {
         --tw-border-opacity: 1;
         border-color: rgb(229 231 235/var(--tw-border-opacity))
         }
         .border-emerald-600 {
         --tw-border-opacity: 1;
         border-color: rgb(5 150 105/var(--tw-border-opacity))
         }
         .border-red-600 {
         --tw-border-opacity: 1;
         border-color: rgb(220 38 38/var(--tw-border-opacity))
         }
         .bg-slate-100 {
         --tw-bg-opacity: 1;
         background-color: rgb(241 245 249/var(--tw-bg-opacity))
         }
         .bg-white {
         --tw-bg-opacity: 1;
         background-color: rgb(255 255 255/var(--tw-bg-opacity))
         }
         .bg-blue-500 {
         --tw-bg-opacity: 1;
         background-color: rgb(59 130 246/var(--tw-bg-opacity))
         }
         .bg-slate-300 {
         --tw-bg-opacity: 1;
         background-color: rgb(203 213 225/var(--tw-bg-opacity))
         }
         .bg-gray-900 {
         --tw-bg-opacity: 1;
         background-color: rgb(17 24 39/var(--tw-bg-opacity))
         }
         .bg-opacity-50 {
         --tw-bg-opacity: 0.5
         }
         .p-1 {
         padding: .25rem
         }
         .p-2 {
         padding: .5rem
         }
         .px-4 {
         padding-left: 1rem;
         padding-right: 1rem
         }
         .py-4 {
         padding-bottom: 1rem;
         padding-top: 1rem
         }
         .py-3 {
         padding-bottom: .75rem;
         padding-top: .75rem
         }
         .py-\[2px\] {
         padding-bottom: 2px;
         padding-top: 2px
         }
         .px-\[6px\] {
         padding-left: 6px;
         padding-right: 6px
         }
         .py-0\.5 {
         padding-bottom: .125rem;
         padding-top: .125rem
         }
         .px-2 {
         padding-left: .5rem;
         padding-right: .5rem
         }
         .py-0 {
         padding-bottom: 0;
         padding-top: 0
         }
         .px-5 {
         padding-left: 1.25rem;
         padding-right: 1.25rem
         }
         .py-1 {
         padding-bottom: .25rem;
         padding-top: .25rem
         }
         .py-2 {
         padding-bottom: .5rem;
         padding-top: .5rem
         }
         .px-3 {
         padding-left: .75rem;
         padding-right: .75rem
         }
         .py-1\.5 {
         padding-bottom: .375rem;
         padding-top: .375rem
         }
         .py-5 {
         padding-bottom: 1.25rem;
         padding-top: 1.25rem
         }
         .pt-3 {
         padding-top: .75rem
         }
         .pb-6 {
         padding-bottom: 1.5rem
         }
         .pt-6 {
         padding-top: 1.5rem
         }
         .pt-4 {
         padding-top: 1rem
         }
         .pr-1 {
         padding-right: .25rem
         }
         .pb-4 {
         padding-bottom: 1rem
         }
         .pr-2 {
         padding-right: .5rem
         }
         .pb-2 {
         padding-bottom: .5rem
         }
         .pl-1 {
         padding-left: .25rem
         }
         .pt-2 {
         padding-top: .5rem
         }
         .text-center {
         text-align: center
         }
         .text-right {
         text-align: right
         }
         .align-middle {
         vertical-align: middle
         }
         .text-sm {
         font-size: .875rem;
         line-height: 1.25rem
         }
         .text-lg {
         font-size: 1.125rem;
         line-height: 1.75rem
         }
         .text-xs {
         font-size: .75rem;
         line-height: 1rem
         }
         .text-\[11px\] {
         font-size: 11px
         }
         .text-\[10px\] {
         font-size: 10px
         }
         .text-\[12px\] {
         font-size: 12px
         }
         .font-semibold {
         font-weight: 600
         }
         .font-medium {
         font-weight: 500
         }
         .text-slate-600 {
         --tw-text-opacity: 1;
         color: rgb(71 85 105/var(--tw-text-opacity))
         }
         .text-green-500 {
         --tw-text-opacity: 1;
         color: rgb(34 197 94/var(--tw-text-opacity))
         }
         .text-blue-500 {
         --tw-text-opacity: 1;
         color: rgb(59 130 246/var(--tw-text-opacity))
         }
         .text-red-500 {
         --tw-text-opacity: 1;
         color: rgb(239 68 68/var(--tw-text-opacity))
         }
         .text-slate-500 {
         --tw-text-opacity: 1;
         color: rgb(100 116 139/var(--tw-text-opacity))
         }
         .text-blue-600 {
         --tw-text-opacity: 1;
         color: rgb(37 99 235/var(--tw-text-opacity))
         }
         .text-slate-800 {
         --tw-text-opacity: 1;
         color: rgb(30 41 59/var(--tw-text-opacity))
         }
         .text-slate-50 {
         --tw-text-opacity: 1;
         color: rgb(248 250 252/var(--tw-text-opacity))
         }
         .text-slate-700 {
         --tw-text-opacity: 1;
         color: rgb(51 65 85/var(--tw-text-opacity))
         }
         .text-gray-700 {
         --tw-text-opacity: 1;
         color: rgb(55 65 81/var(--tw-text-opacity))
         }
         .text-emerald-600 {
         --tw-text-opacity: 1;
         color: rgb(5 150 105/var(--tw-text-opacity))
         }
         .text-red-600 {
         --tw-text-opacity: 1;
         color: rgb(220 38 38/var(--tw-text-opacity))
         }
         .underline {
         text-decoration-line: underline
         }
         .opacity-25 {
         opacity: .25
         }
         .opacity-0 {
         opacity: 0
         }
         .shadow-sm {
         --tw-shadow: 0 1px 2px 0 rgba(0,0,0,.05);
         --tw-shadow-colored: 0 1px 2px 0 var(--tw-shadow-color)
         }
         .shadow-md,.shadow-sm {
         box-shadow: 0 0 #0000,0 0 #0000,var(--tw-shadow);
         box-shadow: var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)
         }
         .shadow-md {
         --tw-shadow: 0 4px 6px -1px rgba(0,0,0,.1),0 2px 4px -2px rgba(0,0,0,.1);
         --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color),0 2px 4px -2px var(--tw-shadow-color)
         }
         .blur {
         --tw-blur: blur(8px)
         }
         .blur,.filter {
         -webkit-filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
         filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)
         }
         .transition-all {
         transition-duration: .15s;
         transition-property: all;
         transition-timing-function: cubic-bezier(.4,0,.2,1)
         }
         .transition-\[opacity\2c margin\] {
         transition-duration: .15s;
         transition-property: opacity,margin;
         transition-timing-function: cubic-bezier(.4,0,.2,1)
         }
         .transition {
         transition-duration: .15s;
         transition-property: color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,-webkit-transform,-webkit-filter,-webkit-backdrop-filter;
         transition-property: color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,backdrop-filter;
         transition-property: color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,backdrop-filter,-webkit-transform,-webkit-filter,-webkit-backdrop-filter;
         transition-timing-function: cubic-bezier(.4,0,.2,1)
         }
         .duration-\[0\.1ms\] {
         transition-duration: .1ms
         }
         .before\:inline-block:before {
         content: var(--tw-content);
         display: inline-block
         }
         .before\:h-3:before {
         content: var(--tw-content);
         height: .75rem
         }
         .before\:w-3:before {
         content: var(--tw-content);
         width: .75rem
         }
         .before\:rounded-full:before {
         border-radius: 9999px;
         content: var(--tw-content)
         }
         .before\:bg-white:before {
         --tw-bg-opacity: 1;
         background-color: rgb(255 255 255/var(--tw-bg-opacity));
         content: var(--tw-content)
         }
         .before\:duration-200:before {
         content: var(--tw-content);
         transition-duration: .2s
         }
         .checked\:bg-none:checked {
         background-image: none
         }
         .checked\:before\:translate-x-3:checked:before {
         --tw-translate-x: 0.75rem;
         content: var(--tw-content);
         -webkit-transform: translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
         transform: translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
         }
         .hover\:bg-gray-50:hover {
         --tw-bg-opacity: 1;
         background-color: rgb(249 250 251/var(--tw-bg-opacity))
         }
         .hover\:bg-gray-100:hover {
         --tw-bg-opacity: 1;
         background-color: rgb(243 244 246/var(--tw-bg-opacity))
         }
         .focus\:border:focus {
         border-width: 1px
         }
         .focus\:border-gray-200:focus {
         --tw-border-opacity: 1;
         border-color: rgb(229 231 235/var(--tw-border-opacity))
         }
         .focus\:border-blue-600:focus {
         --tw-border-opacity: 1;
         border-color: rgb(37 99 235/var(--tw-border-opacity))
         }
         .focus\:outline:focus {
         outline-style: solid
         }
         .focus\:outline-2:focus {
         outline-width: 2px
         }
         .focus\:outline-offset-2:focus {
         outline-offset: 2px
         }
         .focus\:outline-slate-200:focus {
         outline-color: #e2e8f0
         }
         .focus\:ring-0:focus {
         --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
         --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(var(--tw-ring-offset-width)) var(--tw-ring-color);
         box-shadow: var(--tw-ring-offset-shadow),var(--tw-ring-shadow),0 0 #0000;
         box-shadow: var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow,0 0 #0000)
         }
         .focus\:ring-offset-0:focus {
         --tw-ring-offset-width: 0px
         }
         .hs-dropdown.open>.hs-dropdown-open\:opacity-100 {
         opacity: 1
         }
         .hs-dropdown.open>.hs-dropdown-open\:opacity-0 {
         opacity: 0
         }
         .hs-dropdown.open>.hs-dropdown-menu>.hs-dropdown-open\:opacity-100 {
         opacity: 1
         }
         .hs-dropdown.open>.hs-dropdown-menu>.hs-dropdown-open\:opacity-0 {
         opacity: 0
         }
         .dark .dark\:divide-gray-700>:not([hidden])~:not([hidden]) {
         --tw-divide-opacity: 1;
         border-color: rgb(55 65 81/var(--tw-divide-opacity))
         }
         .dark .dark\:border {
         border-width: 1px
         }
         .dark .dark\:border-neutral-700 {
         --tw-border-opacity: 1;
         border-color: rgb(64 64 64/var(--tw-border-opacity))
         }
         .dark .dark\:border-neutral-600 {
         --tw-border-opacity: 1;
         border-color: rgb(82 82 82/var(--tw-border-opacity))
         }
         .dark .dark\:border-neutral-500 {
         --tw-border-opacity: 1;
         border-color: rgb(115 115 115/var(--tw-border-opacity))
         }
         .dark .dark\:bg-neutral-800 {
         --tw-bg-opacity: 1;
         background-color: rgb(38 38 38/var(--tw-bg-opacity))
         }
         .dark .dark\:bg-neutral-900 {
         --tw-bg-opacity: 1;
         background-color: rgb(23 23 23/var(--tw-bg-opacity))
         }
         .dark .dark\:bg-neutral-700 {
         --tw-bg-opacity: 1;
         background-color: rgb(64 64 64/var(--tw-bg-opacity))
         }
         .dark .dark\:bg-neutral-400 {
         --tw-bg-opacity: 1;
         background-color: rgb(163 163 163/var(--tw-bg-opacity))
         }
         .dark .dark\:bg-opacity-80 {
         --tw-bg-opacity: 0.8
         }
         .dark .dark\:text-neutral-200 {
         --tw-text-opacity: 1;
         color: rgb(229 229 229/var(--tw-text-opacity))
         }
         .dark .dark\:text-neutral-400 {
         --tw-text-opacity: 1;
         color: rgb(163 163 163/var(--tw-text-opacity))
         }
         .dark .dark\:text-blue-300 {
         --tw-text-opacity: 1;
         color: rgb(147 197 253/var(--tw-text-opacity))
         }
         .dark .dark\:text-white {
         --tw-text-opacity: 1;
         color: rgb(255 255 255/var(--tw-text-opacity))
         }
         .dark .dark\:text-neutral-50 {
         --tw-text-opacity: 1;
         color: rgb(250 250 250/var(--tw-text-opacity))
         }
         .dark .dark\:hover\:bg-slate-800:hover {
         --tw-bg-opacity: 1;
         background-color: rgb(30 41 59/var(--tw-bg-opacity))
         }
         .dark .dark\:hover\:bg-neutral-800:hover {
         --tw-bg-opacity: 1;
         background-color: rgb(38 38 38/var(--tw-bg-opacity))
         }
         .dark .dark\:hover\:text-white:hover {
         --tw-text-opacity: 1;
         color: rgb(255 255 255/var(--tw-text-opacity))
         }
         .dark .dark\:hover\:text-gray-300:hover {
         --tw-text-opacity: 1;
         color: rgb(209 213 219/var(--tw-text-opacity))
         }
         .dark .dark\:focus\:border-blue-600:focus {
         --tw-border-opacity: 1;
         border-color: rgb(37 99 235/var(--tw-border-opacity))
         }
         /*# sourceMappingURL=main.b9d20f92.css.map*/
      </style>
   </head>
   <body id="home" class="dark">
      <div id="root">
         <div class="min-w-[450px] max-w-[450px]">
            <div class="min-h-[182px]">
               <div class="flex justify-between items-center px-4 pt-6 dark:bg-neutral-800">
                  <div>
                     <p class="text-sm text-slate-600 dark:text-neutral-200">Block Number: <span class="font-semibold">"""


async def get_html(block_number, low, high, average, date, time):
    
    html_content = (txt1+f"""{block_number}</span></p>
                 <p class="text-xs text-slate-500 dark:text-neutral-400">Gas Price Tracker</p>
              </div>
              <div>
                 <p class="text-sm text-slate-600 dark:text-neutral-200">{date}</p>
                 <p class="text-xs text-right text-slate-500 dark:text-neutral-400">{time}</p>
                 </p>
              </div>
           </div>
           <div class="grid grid-cols-3 gap-4 dark:bg-neutral-800 px-4 pt-3 pb-6">
              <div class="border border-slate-200 dark:border-neutral-700 rounded-lg text-center py-4">
                 <p class="text-sm text-slate-600 dark:text-neutral-200 mb-1">😁 Low</p>
                 <p class="text-lg font-semibold text-green-500 text-center">{low}</p>
              </div>
              <div class="border border-slate-200 dark:border-neutral-700 rounded-lg text-center py-4">
                 <p class="text-sm text-slate-600 dark:text-neutral-200 mb-1">😄 Average</p>
                 <p class="text-lg font-semibold text-blue-500 text-center">{average}</p>
              </div>
              <div class="border border-slate-200 dark:border-neutral-700 rounded-lg text-center py-4">
                 <p class="text-sm text-slate-600 dark:text-neutral-200 mb-1">🙂 High</p>
                 <p class="text-lg font-semibold text-red-500 text-center">{high}</p>
              </div>
           </div>
        </div>
     </div>
  </body>
</html>""")
    
    return html_content



async def capture_image(api_key):
    
    eth = Etherscan(api_key=api_key)
    gas_prices = eth.get_gas_oracle()
    high, average, low, block_number = gas_prices['FastGasPrice'], gas_prices['ProposeGasPrice'], gas_prices['SafeGasPrice'], gas_prices['LastBlock']

    
    date = strftime("%d/%m/%Y")
    time = strftime("%H:%M:%S")

    html_content = await get_html(block_number, low, high, average, date, time)
    
    async with playwright.async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(device_scale_factor=6)
        page = await context.new_page()
        await page.set_content(html_content)
        await page.set_viewport_size({'width': 450, 'height': 182})
        await page.screenshot(path='output.png')
        await browser.close()
