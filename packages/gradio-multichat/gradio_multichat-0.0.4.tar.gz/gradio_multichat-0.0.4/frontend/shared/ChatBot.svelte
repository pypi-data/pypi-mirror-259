<script lang="ts">
  import { format_chat_for_sharing } from "./utils";
  import { copy } from "@gradio/utils";

  import { dequal } from "dequal/lite";
  import { beforeUpdate, afterUpdate, createEventDispatcher } from "svelte";
  import { ShareButton } from "@gradio/atoms";
  import { Audio } from "@gradio/audio/shared";
  import { Image } from "@gradio/image/shared";
  import { Video } from "@gradio/video/shared";
  import type { SelectData, LikeData } from "@gradio/utils";
  import { MarkdownCode as Markdown } from "@gradio/markdown";
  import { get_fetchable_url_or_file, type FileData } from "@gradio/client";
  import Copy from "./Copy.svelte";
  import type { I18nFormatter } from "js/app/src/gradio_helper";
  import LikeDislike from "./LikeDislike.svelte";
  import Pending from "./Pending.svelte";

  export let value: [
    { name: string; role: string; avatar: string | null },
    string | { file: FileData; alt_text: string | null } | null,
  ][] = [];
  let old_value:
    | [
        { name: string; role: string; avatar: string | null },
        string | { file: FileData; alt_text: string | null } | null,
      ][]
    | null = null;

  export let latex_delimiters: {
    left: string;
    right: string;
    display: boolean;
  }[];
  export let pending_message = false;
  export let selectable = false;
  export let likeable = false;
  export let show_share_button = false;
  export let rtl = false;
  export let show_copy_button = false;
  export let sanitize_html = true;
  export let bubble_full_width = true;
  export let render_markdown = true;
  export let line_breaks = true;
  export let root: string;
  export let proxy_url: null | string;
  export let i18n: I18nFormatter;
  export let layout: "bubble" | "panel" = "bubble";

  let div: HTMLDivElement;
  let autoscroll: boolean;

  $: adjust_text_size = () => {
    let style = getComputedStyle(document.body);
    let body_text_size = style.getPropertyValue("--body-text-size");
    let updated_text_size;

    switch (body_text_size) {
      case "13px":
        updated_text_size = 14;
        break;
      case "14px":
        updated_text_size = 16;
        break;
      case "16px":
        updated_text_size = 20;
        break;
      default:
        updated_text_size = 14;
        break;
    }

    document.body.style.setProperty(
      "--chatbot-body-text-size",
      updated_text_size + "px"
    );
  };

  $: adjust_text_size();

  const dispatch = createEventDispatcher<{
    change: undefined;
    select: SelectData;
    like: LikeData;
  }>();

  beforeUpdate(() => {
    autoscroll =
      div && div.offsetHeight + div.scrollTop > div.scrollHeight - 100;
  });

  const scroll = (): void => {
    if (autoscroll) {
      div.scrollTo(0, div.scrollHeight);
    }
  };
  afterUpdate(() => {
    if (autoscroll) {
      scroll();
      div.querySelectorAll("img").forEach((n) => {
        n.addEventListener("load", () => {
          scroll();
        });
      });
    }
  });

  $: {
    if (!dequal(value, old_value)) {
      old_value = value;
      dispatch("change");
    }
  }

  function handle_select(
    i: number,
    message: string | { file: FileData; alt_text: string | null } | null
  ): void {
    dispatch("select", {
      index: i,
      value: message,
    });
  }

  function handle_like(
    i: number,
    message: string | { file: FileData; alt_text: string | null } | null,
    selected: string | null
  ): void {
    dispatch("like", {
      index: i,
      value: message,
      liked: selected === "like",
    });
  }
</script>

{#if show_share_button && value !== null && value.length > 0}
  <div class="share-button">
    <ShareButton
      {i18n}
      on:error
      on:share
      formatter={format_chat_for_sharing}
      {value}
    />
  </div>
{/if}

<div
  class={layout === "bubble" ? "bubble-wrap" : "panel-wrap"}
  bind:this={div}
  role="log"
  aria-label="chatbot conversation"
  aria-live="polite"
>
  <div class="message-wrap" class:bubble-gap={layout === "bubble"} use:copy>
    {#if value !== null}
      {#each value as [entity, message], i}
        {#if message !== null}
          <div
            class="message-row {layout} {entity.role === 'user'
              ? 'user-row'
              : 'bot-row'}"
          >
            <div class="avatar-container">
              {#if entity.avatar !== null}
                <Image
                  class="avatar-image, topmargin"
                  src={get_fetchable_url_or_file(
                    entity.avatar,
                    root,
                    proxy_url
                  )}
                  alt="{entity.name} avatar"
                />
              {/if}
              <span class="avatar-label">
                {entity.name}<br />
                <!-- {#if i == 0 || (entity.role !== "user" && layout !== "bubble")} -->

                <!-- {/if} -->
              </span>
            </div>
            <div
              class="message {entity.role === 'user' ? 'user' : 'bot'}"
              class:message-fit={layout === "bubble" && !bubble_full_width}
              class:panel-full-width={layout === "panel"}
              class:message-bubble-border={layout === "bubble"}
              class:message-markdown-disabled={!render_markdown}
              style:text-align={rtl && entity.role === "user"
                ? "left"
                : "right"}
            >
              <button
                data-testid={entity.role === "user" ? "user" : "bot"}
                class:latest={i === value.length - 1}
                class:message-markdown-disabled={!render_markdown}
                style:user-select="text"
                class:selectable
                style:text-align={rtl ? "right" : "left"}
                on:click={() => handle_select(i, message)}
                on:keydown={(e) => {
                  if (e.key === "Enter") {
                    handle_select(i, message);
                  }
                }}
                dir={rtl ? "rtl" : "ltr"}
                aria-label={entity.name +
                  "'s message: " +
                  (typeof message === "string"
                    ? message
                    : `a file of type ${message.file?.mime_type}, ${message.file?.alt_text ?? message.file?.orig_name ?? ""}`)}
              >
                {#if typeof message === "string"}
                  <Markdown
                    {message}
                    {latex_delimiters}
                    {sanitize_html}
                    {render_markdown}
                    {line_breaks}
                    on:load={scroll}
                  />
                {:else if message !== null && message.file?.mime_type?.includes("audio")}
                  <Audio
                    data-testid="chatbot-audio"
                    controls
                    preload="metadata"
                    src={message.file?.url}
                    title={message.alt_text}
                    on:play
                    on:pause
                    on:ended
                  />
                {:else if message !== null && message.file?.mime_type?.includes("video")}
                  <Video
                    data-testid="chatbot-video"
                    controls
                    src={message.file?.url}
                    title={message.alt_text}
                    preload="auto"
                    on:play
                    on:pause
                    on:ended
                  >
                    <track kind="captions" />
                  </Video>
                {:else if message !== null && message.file?.mime_type?.includes("image")}
                  <Image
                    data-testid="chatbot-image"
                    src={message.file?.url}
                    alt={message.alt_text}
                  />
                {:else if message !== null && message.file?.url !== null}
                  <a
                    data-testid="chatbot-file"
                    href={message.file?.url}
                    target="_blank"
                    download={window.__is_colab__
                      ? null
                      : message.file?.orig_name || message.file?.path}
                  >
                    {message.file?.orig_name || message.file?.path}
                  </a>
                {/if}
                {#if (likeable && entity.role !== "user") || (show_copy_button && message && typeof message === "string")}
                  <div class="message-buttons">
                    {#if likeable && entity.role !== "user"}
                      <LikeDislike
                        handle_action={(selected) =>
                          handle_like(i, message, selected)}
                      />
                    {/if}
                    {#if show_copy_button && message && typeof message === "string"}
                      <Copy value={message} />
                    {/if}
                  </div>
                {/if}
              </button>
            </div>
          </div>
        {/if}
      {/each}
      {#if pending_message}
        <Pending {layout} />
      {/if}
    {/if}
  </div>
</div>

<style>
  /* Messages */
  .message {
    position: relative;
    display: flex;
    flex-direction: column;
    align-self: flex-end;
    background: var(--background-fill-secondary);
    width: calc(100% - var(--spacing-xxl));
    color: var(--body-text-color);
    font-size: var(--chatbot-body-text-size);
    overflow-wrap: break-word;
    overflow-x: hidden;
    padding-right: calc(var(--spacing-xxl) + var(--spacing-md));
    padding: calc(var(--spacing-xxl) + var(--spacing-sm));
  }
  .message-wrap {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .bubble-gap {
    gap: calc(var(--spacing-xxl) + var(--spacing-lg));
  }
  .message-bubble-border {
    border-width: 1px;
    border-radius: var(--radius-xxl);
  }
  .message-fit {
    width: fit-content !important;
  }
  .panel-full-width {
    padding: calc(var(--spacing-xxl) * 2);
    width: 100%;
  }
  .message-markdown-disabled {
    white-space: pre-line;
  }

  @media (max-width: 480px) {
    .panel-full-width {
      padding: calc(var(--spacing-xxl) * 2);
    }
  }

  .message-row {
    display: flex;
    flex-direction: row;
    position: relative;
  }

  .message-row.panel.user-row {
    background: var(--color-accent-soft);
  }

  .message-row.panel.bot-row {
    background: var(--background-fill-secondary);
  }

  .message-row:last-of-type {
    margin-bottom: var(--spacing-xxl);
  }

  .user-row.bubble {
    flex-direction: row;
    justify-content: flex-end;
  }
  .message-wrap .message :global(img) {
    margin: var(--size-2);
    max-height: 200px;
  }
  .message-wrap .message :global(a) {
    color: var(--color-text-link);
    text-decoration: underline;
  }

  .message-wrap .bot :global(table),
  .message-wrap .bot :global(tr),
  .message-wrap .bot :global(td),
  .message-wrap .bot :global(th) {
    border: 1px solid var(--border-color-primary);
  }

  .message-wrap .user :global(table),
  .message-wrap .user :global(tr),
  .message-wrap .user :global(td),
  .message-wrap .user :global(th) {
    border: 1px solid var(--border-color-accent);
  }

  /* Lists */
  .message-wrap :global(ol),
  .message-wrap :global(ul) {
    padding-inline-start: 2em;
  }

  /* KaTeX */
  .message-wrap :global(span.katex) {
    font-size: var(--text-lg);
    direction: ltr;
  }

  /* Copy button */
  .message-wrap :global(div[class*="code_wrap"] > button) {
    position: absolute;
    top: var(--spacing-md);
    right: var(--spacing-md);
    z-index: 1;
    cursor: pointer;
    border-bottom-left-radius: var(--radius-sm);
    padding: 5px;
    padding: var(--spacing-md);
    width: 25px;
    height: 25px;
  }

  .message-wrap :global(code > button > span) {
    position: absolute;
    top: var(--spacing-md);
    right: var(--spacing-md);
    width: 12px;
    height: 12px;
  }
  .message-wrap :global(.check) {
    position: absolute;
    top: 0;
    right: 0;
    opacity: 0;
    z-index: var(--layer-top);
    transition: opacity 0.2s;
    background: var(--background-fill-primary);
    padding: var(--size-1);
    width: 100%;
    height: 100%;
    color: var(--body-text-color);
  }

  .message-wrap :global(pre) {
    position: relative;
  }

  .message-wrap > .message-row.panel {
    border-bottom: rgb(139, 139, 139) solid 1px;
  }

  .user {
    align-self: flex-start;
    border-bottom-right-radius: 0;
    text-align: right;
    /* Colors */
    border-color: var(--border-color-accent-subdued);
    background-color: var(--color-accent-soft);
  }
  .bot {
    border-bottom-left-radius: 0;
    text-align: left;
    /* Colors */
    border-color: var(--border-color-primary);
    background: var(--background-fill-secondary);
  }

  .bubble-wrap {
    padding: var(--block-padding);
    width: 100%;
    overflow-y: auto;
  }

  .panel-wrap {
    width: 100%;
    overflow-y: auto;
  }

  @media (max-width: 480px) {
    .user-row.bubble {
      align-self: flex-end;
    }

    .bot-row.bubble {
      align-self: flex-start;
    }
    .message {
      width: auto;
    }
  }

  .avatar-container {
    position: sticky;
    align-self: end;
    top: 20px;
    bottom: 20px;
    width: 64px;
    height: 64px;
    z-index: 2;
    place-content: center;
    flex-flow: wrap;
    margin-top: 20px;
    margin-bottom: 20px;
    margin-left: 6px;
    text-align: center;
    font-size: var(--text-lg);
    font-weight: 600;
  }

  .user-row.bubble > .avatar-container {
    order: 2;
    margin-left: 10px;
  }

  .bot-row.bubble > .avatar-container {
    margin-right: 10px;
  }

  .panel > .avatar-container {
    align-self: start;
  }

  .avatar-container :global(img) {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
  }

  .message-buttons {
    display: flex;
    position: relative;
    margin-top: 1rem;
    border-radius: var(--radius-sm);
    justify-content: flex-start;
    bottom: -0.75rem;
    flex-wrap: wrap;
    align-items: center;
  }

  .user-row.bubble .message-buttons {
    justify-content: flex-end;
  }

  .share-button {
    position: absolute;
    top: 4px;
    right: 6px;
  }

  .selectable {
    cursor: pointer;
  }

  @keyframes dot-flashing {
    0% {
      opacity: 0.8;
    }
    50% {
      opacity: 0.5;
    }
    100% {
      opacity: 0.8;
    }
  }
</style>
