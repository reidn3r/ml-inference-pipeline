import { z } from "zod";

export const InferenceRequestSchema = {
  body: z.object({
    model: z.string(),
    text: z.string(),
  }),
};

export type InferenceRequestType = z.infer<typeof InferenceRequestSchema.body>;

export type InferenceRequestMessage = InferenceRequestType & { id: string };